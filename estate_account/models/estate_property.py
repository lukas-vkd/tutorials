from odoo import models

class estate_property(models.Model):
    _inherit = "estate.property"
    



    
    def action_sold(self):
        res = super().action_sold()
        
        journal = self.env["account.move"].with_context(default_move_type="out_invoice")._get_default_journal()
        

        return res