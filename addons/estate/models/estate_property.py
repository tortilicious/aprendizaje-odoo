from datetime import timedelta

from odoo import api, fields, models


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
    )
    active = fields.Boolean(default=True)

    # Computed fields

    total_area = fields.Integer(compute="_compute_total_area", string="Total Area(sqm)")

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    best_price = fields.Integer(compute="_compute_best_price", string="Best Offer")

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

    # Buttons functions
    def action_sell(self):
        if self.state != "cancelled":
            self.state = "sold"

    def action_cancel(self):
        if self.state != "sold":
            self.state = "cancelled"