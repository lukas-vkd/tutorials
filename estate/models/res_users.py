from odoo import fields, models

class users(models.Model):
    _inherit = "res.users"
    
    property_ids = fields.One2many(
        "estate.property", "sales_person_id", string="Properties", domain=[("state", "in", ["new", "offer_received"])]
    )