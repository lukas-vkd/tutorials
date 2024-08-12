from odoo import fields, models, api

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "represents a type a property can be (Many2One)"
    _order = "sequence, name"
    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)',
         'The name of the type must be unique')
    ]
    
    sequence = fields.Integer('Sequence', default=1, help="Used to order types, house is prefered")
    name = fields.Char("Type", required=True)
    offer_count = fields.Integer(string="Offers Count", compute="_compute_offers")
    property_ids = fields.One2many("estate.property", inverse_name="property_type_id")
    offer_ids = fields.One2many("estate.property.offer", string="Offers", inverse_name="property_type_id")

    
    @api.depends("offer_ids")
    def _compute_offers(self):
        #there has got to be a better way
        count = 0
        for record in self:
            for offer in record.offer_ids:
                count = count + 1           
        
        self.offer_count = count
        