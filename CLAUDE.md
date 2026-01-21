# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Docker-based development environment for Odoo ERP with PostgreSQL. Uses Docker Compose for orchestration with automatic database initialization and admin credential configuration.

## Common Commands

```bash
# Start services (first run initializes DB and admin user)
docker compose up -d

# Rebuild image (required after changes to Dockerfile or requirements.txt)
docker compose build odoo
docker compose up -d --build      # Build and start in one command

# View logs
docker compose logs -f odoo       # Odoo logs
docker compose logs -f db         # PostgreSQL logs

# Restart Odoo (required after Python code changes)
docker compose restart odoo

# Access container shells
docker compose exec odoo bash
docker compose exec db psql -U odoo -d odoo

# Full reset (deletes all data)
docker compose down -v && docker compose up -d
```

## Architecture

**Services (docker-compose.yml):**
- `db`: PostgreSQL database (image version via `$POSTGRES_IMAGE`)
- `odoo`: Odoo application server (image version via `$ODOO_IMAGE`)

**Key Files:**
- `Dockerfile`: Custom Odoo image with uv package manager and Python dependencies from `addons/requirements.txt`
- `scripts/entrypoint.sh`: Custom entrypoint that handles first-run initialization (installs base modules, loads demo data if `ODOO_LOAD_DEMO=true`, sets admin credentials) and automatic module management via `ODOO_AUTO_INSTALL`, `ODOO_AUTO_UPDATE`, and `ODOO_DEV_MODULES`
- `scripts/lint.sh`: Code quality verification script (ruff + ty)
- `config/odoo.conf`: Odoo configuration optimized for development
- `config/postgresql.conf`: PostgreSQL configuration optimized for performance
- `.env`: Environment variables for credentials and image versions (copy from `.env.example`)
- `addons/requirements.txt`: Python dependencies for custom modules (rebuild image after changes)

**Volume Mounts:**
- `./addons` → `/mnt/extra-addons`: Custom Odoo modules
- `./config/odoo.conf` → `/etc/odoo/odoo.conf`: Configuration file
- `./config/postgresql.conf` → `/etc/postgresql/postgresql.conf`: Database configuration
- `./scripts/entrypoint.sh` → `/entrypoint.sh`: Initialization script

## Development Workflow

**Module Development:**
1. Create modules in `addons/` directory (each module needs `__init__.py` and `__manifest__.py`)
2. XML changes are hot-reloaded (dev mode enabled)
3. Python changes require `docker compose restart odoo`

**Automatic Module Management (in `.env`):**
| Variable | Description |
|----------|-------------|
| `ODOO_LOAD_DEMO=true` | Load demo data during initial database setup |
| `ODOO_AUTO_INSTALL=true` | Auto-install new modules from `addons/` not yet installed in Odoo |
| `ODOO_AUTO_UPDATE=true` | Auto-update modules with files modified after last Odoo update |
| `ODOO_DEV_MODULES=mod1,mod2` | Always update these modules on restart (manual override) |

**Database Access:**
- PostgreSQL exposed on port 5432 for external tools
- Connect with: `psql -h localhost -U odoo -d odoo`

**Odoo Access:**
- Web interface: `http://localhost:8069` (or port set in `$ODOO_PORT`)
- XML-RPC enabled for external integrations

## Configuration Notes

- Admin credentials (`ODOO_ADMIN_EMAIL`, `ODOO_ADMIN_PASSWORD`) only apply on first initialization
- `admin_passwd` in odoo.conf is the master password for database management UI
- Demo data enabled by default (`ODOO_LOAD_DEMO=true`), set to `false` for empty database

## Performance Configuration

Configurations are optimized for: **AMD Ryzen 5 5600X (12 threads) + 31GB RAM + SSD**

**Odoo (`config/odoo.conf`):**
- `workers = 0`: Single-thread mode for easier debugging
- `limit_memory_soft = 6GB`: Soft memory limit per worker
- `limit_memory_hard = 8GB`: Hard memory limit per worker
- `limit_time_cpu = 1800s`: CPU time limit for long operations
- `limit_time_real = 3600s`: Real time limit for long operations

**PostgreSQL (`config/postgresql.conf`):**
- `shared_buffers = 8GB`: Main cache (25% of RAM)
- `effective_cache_size = 24GB`: OS cache estimate (75% of RAM)
- `work_mem = 256MB`: Memory for sort/hash operations
- `maintenance_work_mem = 1GB`: Memory for VACUUM, CREATE INDEX
- `max_parallel_workers = 12`: Parallelism matching CPU threads
- `random_page_cost = 1.1`: Optimized for SSD
- `effective_io_concurrency = 200`: Parallel I/O for SSD
- `log_min_duration_statement = 1000`: Log slow queries (>1s)

To adjust for different hardware, modify these files and restart services with `docker compose down && docker compose up -d`.
