from odoo import fields, models

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "represents a tag a property can be (Many2Many)"
    _order = "name"

    name = fields.Char("Tag", required=True)
    

    
    color = fields.Integer()
    
    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)',
         'The name of the tag must be unique')
    ]