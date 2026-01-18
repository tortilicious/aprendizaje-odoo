from datetime import timedelta

from odoo import api, fields, models
from odoo.exceptions import UserError


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"

    partner_id = fields.Many2one(
        comodel_name="res.partner",
        required=True,
        string="Partner",
    )
    property_id = fields.Many2one(
        comodel_name="estate.property",
        required=True,
        string="Property",
        ondelete="cascade",
    )

    price = fields.Float(string="Price")
    status = fields.Selection(
        [
            ("accepted", "Accepted"),
            ("refused", "Refused"),
        ],
        string="Status",
    )

    validity = fields.Integer(string="Validity (days)", default=7)

    # COMPUTED FIELDS

    date_deadline = fields.Date(
        string="Deadline",
        compute="_compute_date_deadline",
        inverse="_inverse_date_deadline",
    )

    @api.depends("create_date", "validity")
    def _compute_date_deadline(self):
        for record in self:
            create_date = record.create_date.date() if record.create_date else fields.Date.today()
            record.date_deadline = create_date + timedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            create_date = record.create_date.date() if record.create_date else fields.Date.today()
            record.validity = (record.date_deadline - create_date).days

    # ONCHANGE METHODS

    @api.onchange("date_deadline")
    def _onchange_date_deadline(self):
        if self.date_deadline:
            today = fields.Date.today()

            # Si elige fecha pasada, forzar a hoy
            if self.date_deadline < today:
                self.date_deadline = today

            create_date = self.create_date.date() if self.create_date else today
            self.validity = (self.date_deadline - create_date).days

    # CRUD HOOKS: Estos métodos se ejecutan automáticamente en momentos específicos

    @api.model_create_multi
    def create(self, vals_list):
        """
        Se ejecuta cuando se crean nuevas ofertas.

        Después de crear las ofertas, actualizamos el estado de las propiedades
        relacionadas para que reflejen que han recibido ofertas.
        """
        # Llamamos a la función original de create para crear los registros
        offers = super().create(vals_list)

        # Agrupamos las ofertas por propiedad para optimizar
        # (si creamos 5 ofertas para la misma propiedad, solo actualizamos una vez)
        properties = offers.mapped("property_id")

        # Actualizamos el estado de cada propiedad afectada
        properties._update_state_from_offers()

        return offers

    def write(self, vals):
        """
        Se ejecuta cuando se modifican ofertas existentes.

        Si se modifica el campo 'status' (aceptar/rechazar oferta),
        actualizamos el estado de la propiedad relacionada.
        """
        # Guardamos las propiedades afectadas ANTES de hacer cambios
        # (por si acaso el write modifica property_id, aunque es raro)
        properties = self.mapped("property_id")

        # Llamamos a la función original de write
        result = super().write(vals)

        # Si se modificó el status, actualizamos estados de propiedades
        if "status" in vals:
            # Validación adicional: solo puede haber una oferta aceptada por propiedad
            if vals.get("status") == "accepted":
                self._validate_single_accepted_offer()

            properties._update_state_from_offers()

        return result

    def unlink(self):
        """
        Se ejecuta cuando se eliminan ofertas.

        Guardamos referencias a las propiedades afectadas antes de eliminar
        las ofertas, para poder actualizar sus estados después.
        """
        # IMPORTANTE: Guardar las propiedades ANTES de eliminar las ofertas
        # porque después de unlink() ya no podremos acceder a property_id
        properties = self.mapped("property_id")

        # Llamamos al método original de unlink
        result = super().unlink()

        # Actualizamos estados después de la eliminación
        properties._update_state_from_offers()

        return result

    # VALIDATION METHODS

    def _validate_single_accepted_offer(self):
        """
        Valida que solo haya una oferta aceptada por propiedad.

        Esta validación se ejecuta antes de aceptar una nueva oferta.
        Si ya existe una oferta aceptada para la misma propiedad, lanza un error.
        """
        for offer in self:
            # Obtener todas las otras ofertas de la misma propiedad
            other_offers = offer.property_id.offer_ids.filtered(lambda o: o.id != offer.id)

            # Buscar si alguna ya está aceptada
            other_accepted_offer = other_offers.filtered(lambda o: o.status == "accepted")

            if other_accepted_offer:
                raise UserError(
                    f"This property already has an accepted offer from "
                    f"{other_accepted_offer[0].partner_id.name}. "
                    f"Please refuse the current offer before accepting a new one."
                )

    # ACTION BUTTONS

    def action_accept_offer(self):
        """
        Acepta la oferta actual.

        Esta función se ejecuta cuando el usuario hace clic en el botón de aceptar
        en la vista de lista de ofertas.

        La función write() se encargará automáticamente de:
        - Validar que no haya otra oferta aceptada (vía _validate_single_accepted_offer)
        - Actualizar el estado de la propiedad (vía _update_state_from_offers)
        """
        for offer in self:
            # Validar que la propiedad no esté en un estado final
            if offer.property_id.state in ("sold", "cancelled"):
                raise UserError(
                    f"Cannot accept offer for property '{offer.property_id.name}' "
                    f"because it is already {offer.property_id.state}."
                )

            # Cambiar el status de la oferta a 'accepted'
            # Esto disparará el hook write() que:
            # 1. Validará que no haya otra oferta aceptada
            # 2. Actualizará el estado de la propiedad automáticamente
            offer.write({"status": "accepted"})

            # Solo si la validación pasó, actualizar el selling_price de la propiedad
            offer.property_id.write({"selling_price": offer.price})

    def action_refuse_offer(self):
        """
        Rechaza la oferta actual.

        Esta función se ejecuta cuando el usuario hace clic en el botón de rechazar
        en la vista de lista de ofertas.

        La función write() se encargará automáticamente de actualizar el estado
        de la propiedad (vía _update_state_from_offers).
        """
        for offer in self:
            # Validar que la propiedad no esté en un estado final
            if offer.property_id.state in ("sold", "cancelled"):
                raise UserError(
                    f"Cannot refuse offer for property '{offer.property_id.name}' "
                    f"because it is already {offer.property_id.state}."
                )

            # Cambiar el status a 'refused'
            # El hook write() actualizará automáticamente el estado de la propiedad
            offer.write({"status": "refused"})
