#!/bin/bash
set -e

# Esperar a que PostgreSQL esté listo
until pg_isready -h db -U ${POSTGRES_USER} -d ${POSTGRES_DB}; do
  echo "Esperando a PostgreSQL..."
  sleep 2
done

# Verificar si la base de datos ya tiene tablas de Odoo
TABLE_COUNT=$(PGPASSWORD=${POSTGRES_PASSWORD} psql -h db -U ${POSTGRES_USER} -d ${POSTGRES_DB} -tAc "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'public';")

if [ "$TABLE_COUNT" -eq "0" ]; then
  echo "Base de datos vacía. Inicializando Odoo con módulo base..."
  odoo -c /etc/odoo/odoo.conf \
       --db_host=db \
       --db_user=${POSTGRES_USER} \
       --db_password=${POSTGRES_PASSWORD} \
       --database=${POSTGRES_DB} \
       -i base \
       --stop-after-init

  echo "Configurando credenciales del administrador..."

  # Actualizar email y contraseña del usuario admin usando SQL
  # Odoo almacena las contraseñas hasheadas, así que usamos la función de Odoo para esto
  PGPASSWORD=${POSTGRES_PASSWORD} psql -h db -U ${POSTGRES_USER} -d ${POSTGRES_DB} -c \
    "UPDATE res_users SET login='${ODOO_ADMIN_EMAIL}' WHERE id=2;"

  # Para la contraseña, necesitamos ejecutar un comando de Odoo porque usa hashing
  odoo shell -c /etc/odoo/odoo.conf \
             --db_host=db \
             --db_user=${POSTGRES_USER} \
             --db_password=${POSTGRES_PASSWORD} \
             --database=${POSTGRES_DB} \
             --no-http <<EOF
env['res.users'].browse(2).write({'password': '${ODOO_ADMIN_PASSWORD}'})
env.cr.commit()
EOF

  echo "Inicialización completada. Usuario: ${ODOO_ADMIN_EMAIL}"
fi

# Función para obtener módulos no instalados de /mnt/extra-addons
get_uninstalled_modules() {
  local modules_to_install=""

  for dir in /mnt/extra-addons/*/; do
    if [ -d "$dir" ] && [ -f "${dir}__manifest__.py" ]; then
      module_name=$(basename "$dir")

      is_installed=$(PGPASSWORD=${POSTGRES_PASSWORD} psql -h db -U ${POSTGRES_USER} -d ${POSTGRES_DB} -tAc \
        "SELECT COUNT(*) FROM ir_module_module WHERE name='${module_name}' AND state='installed';" 2>/dev/null || echo "0")

      if [ "$is_installed" = "0" ]; then
        if [ -z "$modules_to_install" ]; then
          modules_to_install="$module_name"
        else
          modules_to_install="$modules_to_install,$module_name"
        fi
      fi
    fi
  done

  echo "$modules_to_install"
}

# Función para obtener módulos instalados que tienen cambios en sus archivos
# Compara la fecha de última modificación de archivos con write_date en Odoo
get_modules_with_changes() {
  local modules_to_update=""

  for dir in /mnt/extra-addons/*/; do
    if [ -d "$dir" ] && [ -f "${dir}__manifest__.py" ]; then
      module_name=$(basename "$dir")

      # Obtener write_date del módulo en Odoo (epoch timestamp)
      module_write_date=$(PGPASSWORD=${POSTGRES_PASSWORD} psql -h db -U ${POSTGRES_USER} -d ${POSTGRES_DB} -tAc \
        "SELECT EXTRACT(EPOCH FROM write_date)::bigint FROM ir_module_module WHERE name='${module_name}' AND state='installed';" 2>/dev/null)

      # Si el módulo está instalado y tiene write_date
      if [ -n "$module_write_date" ] && [ "$module_write_date" != "" ]; then
        # Obtener timestamp del archivo más reciente en el módulo (excluyendo __pycache__ y .pyc)
        latest_file_date=$(find "$dir" -type f \( -name "*.py" -o -name "*.xml" -o -name "*.csv" -o -name "*.js" -o -name "*.css" -o -name "*.scss" \) -printf '%T@\n' 2>/dev/null | sort -n | tail -1 | cut -d. -f1)

        if [ -n "$latest_file_date" ] && [ "$latest_file_date" -gt "$module_write_date" ]; then
          if [ -z "$modules_to_update" ]; then
            modules_to_update="$module_name"
          else
            modules_to_update="$modules_to_update,$module_name"
          fi
        fi
      fi
    fi
  done

  echo "$modules_to_update"
}

# Determinar qué módulos instalar y actualizar
MODULES_TO_INSTALL=""
MODULES_TO_UPDATE=""

# ODOO_AUTO_INSTALL=true → instalar módulos no instalados de /mnt/extra-addons
if [ "$ODOO_AUTO_INSTALL" = "true" ]; then
  UNINSTALLED_MODULES=$(get_uninstalled_modules)
  if [ -n "$UNINSTALLED_MODULES" ]; then
    echo "ODOO_AUTO_INSTALL: Módulos no instalados detectados: $UNINSTALLED_MODULES"
    MODULES_TO_INSTALL="$UNINSTALLED_MODULES"
  fi
fi

# ODOO_AUTO_UPDATE=true → actualizar módulos con cambios en archivos
if [ "$ODOO_AUTO_UPDATE" = "true" ]; then
  CHANGED_MODULES=$(get_modules_with_changes)
  if [ -n "$CHANGED_MODULES" ]; then
    echo "ODOO_AUTO_UPDATE: Módulos con cambios detectados: $CHANGED_MODULES"
    MODULES_TO_UPDATE="$CHANGED_MODULES"
  fi
fi

# ODOO_DEV_MODULES → siempre actualizar estos módulos (comportamiento manual)
if [ -n "$ODOO_DEV_MODULES" ]; then
  echo "ODOO_DEV_MODULES: Módulos a actualizar: $ODOO_DEV_MODULES"
  if [ -n "$MODULES_TO_UPDATE" ]; then
    MODULES_TO_UPDATE="$MODULES_TO_UPDATE,$ODOO_DEV_MODULES"
  else
    MODULES_TO_UPDATE="$ODOO_DEV_MODULES"
  fi
fi

# Construir argumentos de Odoo
ODOO_ARGS="-c /etc/odoo/odoo.conf --db_host=db --db_user=${POSTGRES_USER} --db_password=${POSTGRES_PASSWORD} --database=${POSTGRES_DB} --dev=xml"

if [ -n "$MODULES_TO_INSTALL" ]; then
  echo ">>> Instalando módulos: $MODULES_TO_INSTALL"
  ODOO_ARGS="$ODOO_ARGS -i $MODULES_TO_INSTALL"
fi

if [ -n "$MODULES_TO_UPDATE" ]; then
  echo ">>> Actualizando módulos: $MODULES_TO_UPDATE"
  ODOO_ARGS="$ODOO_ARGS -u $MODULES_TO_UPDATE"
fi

if [ -z "$MODULES_TO_INSTALL" ] && [ -z "$MODULES_TO_UPDATE" ]; then
  echo ">>> No hay módulos para instalar o actualizar."
fi

# Arrancar Odoo
exec odoo $ODOO_ARGS