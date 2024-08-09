from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "represents a type a property can be (Many2One)"
    _order = "name"

    name = fields.Char("Type", required=True)
    
    
    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)',
         'The name of the type must be unique')
    ]
    
    property_ids = fields.One2many("estate.property", inverse_name="property_type_id")