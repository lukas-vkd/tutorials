from odoo import fields, models, api

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "represents a type a property can be (Many2One)"
    _order = "sequence, name"
    
    sequence = fields.Integer('Sequence', default=1, help="Used to order types, house is prefered")

    name = fields.Char("Type", required=True)
    
    
    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)',
         'The name of the type must be unique')
    ]
    
    property_ids = fields.One2many("estate.property", inverse_name="property_type_id")
    
    offer_ids = fields.One2many("estate.property.offer", string="Offers", inverse_name="property_type_id")

    offer_count = fields.Integer(string="Offers Count", compute="_count_offers")
    
    @api.depends("offer_ids")
    def _count_offers(self):
        count = 0
        for record in self:
            for offer in record.offer_ids:
                count = count + 1           
        
        self.offer_count = count