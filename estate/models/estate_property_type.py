from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "represents a type a property can be"
    name = fields.Char('Type', required=True)
    