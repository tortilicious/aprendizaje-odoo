from datetime import timedelta

from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    property_type_id = fields.Many2one(
        comodel_name="estate.property.type",
        string="Property Type",
    )

    buyer_id = fields.Many2one(comodel_name="res.partner", string="Buyer", index=True, copy=False)

    seller_id = fields.Many2one(
        comodel_name="res.users", string="Salesperson", index=True, default=lambda self: self.env.user
    )

    tag_ids = fields.Many2many(
        comodel_name="estate.property.tag",
        string="Property Tags",
    )

    offer_ids = fields.One2many(
        comodel_name="estate.property.offer",
        inverse_name="property_id",
        string="Offers",
    )

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(
        string="Available From", copy=False, default=lambda self: fields.Date.today() + timedelta(days=90)
    )
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(string="Living Area(sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(string="Garden Area(sqm)")
    garden_orientation = fields.Selection(
        [
            ("north", "North"),
            ("south", "South"),
            ("east", "East"),
            ("west", "West"),
        ]
    )
    state = fields.Selection(
        [
            ("new", "New"),
            ("offer_received", "Offer received"),
            ("offer_accepted", "Offer accepted"),
            ("sold", "Sold"),
            ("cancelled", "Cancelled"),
        ],
        string="Status",
        default="new",
        readonly=True,
    )
    active = fields.Boolean(default=True)
    total_area = fields.Integer(compute="_compute_total_area", string="Total Area(sqm)")
    best_price = fields.Integer(compute="_compute_best_price", string="Best Offer")

    # SQL CONSTRAINTS

    _sql_constraints = [
        (
            "check_expected_price_positive",
            "CHECK(expected_price > 0)",
            "The expected price must be positive.",
        ),
        (
            "check_selling_price_positive",
            "CHECK(selling_price >= 0)",
            "The selling_price must be positive.",
        ),
    ]

    # COMPUTED CONSTRAINTS
    @api.constrains("selling_price", "expected_price")
    def _check_minimum_price(self):
        """
        Verifica que el precio de venta no sea menor al 90% del precio esperado.

        Este constraint se ejecuta automáticamente cada vez que se modifica
        selling_price o expected_price en cualquier registro.
        """
        for record in self:
            # Importante: selling_price es 0 hasta que se acepta una oferta
            # Solo validamos cuando selling_price > 0 (es decir, cuando hay una venta real)
            if record.selling_price > 0 and record.selling_price < 0.9 * record.expected_price:
                raise ValidationError(
                    "The selling price cannot be lower than 90% of the expected price. "
                    f"Expected price: {record.expected_price:,.2f}, "
                    f"Minimum acceptable: {0.9 * record.expected_price:,.2f}, "
                    f"Current selling price: {record.selling_price:,.2f}"
                )

    # COMPUTED FIELDS

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids")
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped("price"), default=0)

    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = "north"
        else:
            self.garden_area = 0
            self.garden_orientation = None

    # HELPER FUNCTION
    def _update_state_from_offers(self):
        """
        Función auxiliar que actualiza el estado de la propiedad basándose en las ofertas.

        Reglas de negocio:
        - Si hay alguna oferta aceptada -> 'offer_accepted'
        - Si hay ofertas pendientes (sin aceptar/rechazar) -> 'offer_received'
        - Si no hay ofertas o todas están rechazadas -> 'new'

        Esta función NO se ejecuta si la propiedad está en estado 'sold' o 'cancelled'
        porque esos son estados finales que no deben cambiar.
        """
        for record in self:
            if record.state in ("cancelled", "sold"):
                continue

            accepted_offers = record.offer_ids.filtered(lambda offer: offer.status == "accepted")
            if accepted_offers:
                record.state = "offer_accepted"
                continue

            pending_offers = record.offer_ids.filtered(lambda offer: not offer.status)
            if pending_offers:
                record.state = "offer_received"
                continue

            record.state = "new"

    # ACTION BUTTONS
    def action_sell(self):
        """
        Marca la propiedad como vendida.
        Validaciones:
        - No se puede vender una propiedad ya cancelada
        - El estado cambia a 'sold' de forma permanente
        """
        for record in self:
            if record.state == "cancelled":
                raise UserError("Cannot sell a cancelled property.")
            # Cambiamos el estado a 'sold' usando write() para evitar restricciones de readonly
            record.write({"state": "sold"})

    def action_cancel(self):
        """
        Marca la propiedad como cancelada.
        Validaciones:
        - No se puede cancelar una propiedad ya vendida
        - El estado cambia a 'cancelled' de forma permanente
        """

        for record in self:
            if record.state == "sold":
                raise UserError("Cannot cancel a sold property.")
            # Cambiamos el estado a 'cancelled' usando write() para evitar restricciones de readonly
            record.write({"state": "cancelled"})
