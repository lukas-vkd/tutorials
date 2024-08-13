from odoo import models, Command

class estate_property(models.Model):
    _inherit = "estate.property"
    
    
    def action_sold(self):
        
        #TODO: test this
        self.env["account.move"].check_access_rights("write")
        self.env["account.move"].check_access_rule("write")
        
        print(" reached ".center(100, '='))
        
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
            
        
        
        journal = self.env["account.move"].sudo().create(invoice_vals)


        return super(estate_property, self).action_sold()