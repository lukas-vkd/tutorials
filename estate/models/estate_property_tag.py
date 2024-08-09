from odoo import fields, models

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "represents a tag a property can be (Many2Many)"
    name = fields.Char("Tag", required=True)
    
    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)',
         'The name of the tag must be unique')
    ]