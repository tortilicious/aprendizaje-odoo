from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property_type"
    _description = "Estate Property Type"

    partner_id = fields.Many2one("res.partner", string="Partner", help="Property owner")
    name = fields.Char(string="Property Type" , required=True)
