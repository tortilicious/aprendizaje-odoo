from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tag"

    name = fields.Char()

    # SQL CONSTRAINTS
    _sql_constraints = [
        # No puede haber dos tags con el mismo nombre
        (
            "unique_tag_name",
            "UNIQUE(name)",
            "A tag with this name already exists. Tag names must be unique.",
        ),
    ]