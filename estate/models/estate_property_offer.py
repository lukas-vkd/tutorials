from odoo import fields, models

class EstatePropertyTag(models.Model):
    _name = "estate.property.offer"
    _description = "represents an offer to buy the property"
    price = fields.Float()
    status = fields.Selection(
        string="Status",
        selection=[("accepted", "Accepted"), ("refused", "Refused")],
        help="Type is used to describe the status of the offer")
    
    partner_id = fields.Many2one("res.partner", string="buyer", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)
