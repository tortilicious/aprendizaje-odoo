from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type"

    estate_property_ids = fields.One2many(
        comodel_name="estate.property",
        inverse_name="property_type_id",
        string="Properties"
    )
    name = fields.Char(required=True)

    # SQL CONSTRAINTS
    _sql_constraints = [
        # No puede haber dos tipos de propiedad con el mismo nombre
        (
            "unique_property_type_name",
            "UNIQUE(name)",
            "A property type with this name already exists. Property type names must be unique.",
        ),
    ]