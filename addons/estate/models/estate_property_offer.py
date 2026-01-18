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

    # Computed fields

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

    @api.onchange("date_deadline")
    def _onchange_date_deadline(self):
        if self.date_deadline:
            today = fields.Date.today()

            # Si elige fecha pasada, forzar a hoy
            if self.date_deadline < today:
                self.date_deadline = today

            create_date = self.create_date.date() if self.create_date else today
            self.validity = (self.date_deadline - create_date).days

    # Buttons functions
    def action_accept_offer(self):
        # Validar que no haya otra oferta aceptada
        accepted_offer = self.property_id.offer_ids.filtered(lambda o: o.status == 'accepted')
        if accepted_offer:
            raise UserError(
                "There is an already accepted offer for this property. "
                "You cannot accept this offer before you refuse the other one."
            )

        # Rechazar todas las demás ofertas
        other_offers = self.property_id.offer_ids.filtered(lambda o: o.id != self.id)
        other_offers.write({"status": "refused"})

        # Aceptar esta oferta
        self.status = "accepted"
        self.property_id.buyer_id = self.partner_id
        self.property_id.selling_price = self.price
        self.property_id.state = "offer_accepted"

    def action_refuse_offer(self):
        self.status = "refused"
        self.property_id.selling_price = 0
        self.property_id.buyer_id = None
