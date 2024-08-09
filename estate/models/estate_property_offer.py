from dateutil.relativedelta import relativedelta
import datetime

from odoo import api, fields, models

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "represents an offer to buy the property"
    price = fields.Float()
    status = fields.Selection(
        string="Status",
        selection=[("accepted", "Accepted"), ("refused", "Refused")],
        help="Type is used to describe the status of the offer")
    
    partner_id = fields.Many2one("res.partner", string="buyer", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)

    validity = fields.Integer(string="numbers of days the offer is valid", default=7)
    date_deadline = fields.Date(string="date by which the offer expires", compute="_compute_date_deadline", inverse="_inverse_date_deadline")
    
    @api.depends("validity")
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = fields.Date.today() + relativedelta(day=+ record.validity)
    
    def _inverse_date_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - fields.Date.today()).days