from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "represents a type a property can be (Many2One)"
    name = fields.Char("Type", required=True)
    