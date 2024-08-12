from odoo import models, Command

class estate_property(models.Model):
    _inherit = "estate.property"
    
    
    def action_sold(self):
        res = super().action_sold()
        
        invoice_vals = {
            "partner_id": self.buyer_id.id,
            "move_type": "out_invoice",
            
            "line_ids": [
                Command.create({
                    "name": "Commision",
                    "quantity": 1,
                    "price_unit": self.selling_price * 0.06
                }),
                Command.create({
                    "name": "admin fees",
                    "quantity": 1,
                    "price_unit": 100.00
                })
            ],
        }
            
        
        
        journal = self.env["account.move"].create(invoice_vals)


        return super(estate_property, self).action_sold()