from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, exceptions

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "an offer to buy a property (Many2one)"
    _order = "price desc"
    _sql_constraints = [
        ('check_price', 'CHECK(price > 0)',
         'The offered price must be positive')
    ]
    
    
    price = fields.Float()
    status = fields.Selection(
        string="Status",
        selection=[("accepted", "Accepted"), ("refused", "Refused")],
        help="Type is used to describe the status of the offer")
    validity = fields.Integer(string="numbers of days the offer is valid", default=7)
    date_deadline = fields.Date(string="date by which the offer expires", compute="_compute_date_deadline", inverse="_inverse_date_deadline")

    
    partner_id = fields.Many2one("res.partner", string="buyer", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)
    property_type_id = fields.Many2one(
        "estate.property.type", related="property_id.property_type_id", string="Property Type", store=True
    )
    
    
    @api.depends("create_date", "validity")
    def _compute_date_deadline(self):
        for offer in self:
            date = offer.create_date.date() if offer.create_date else fields.Date.today()
            offer.date_deadline = date + relativedelta(days=offer.validity)

    def _inverse_date_deadline(self):
        for offer in self:
            date = offer.create_date.date() if offer.create_date else fields.Date.today()
            offer.validity = (offer.date_deadline - date).days

    
    #CRUD methods
    
    @api.model
    def create(self, vals):
        
        offer_property = self.env["estate.property"].browse(vals["property_id"])

        # use library to compare floats
        if vals["price"] < offer_property.best_price:
            raise exceptions.UserError("You can't make an offer lower than the highest offer")
       
        offer_property.state = "offer_received"
       
        return super().create(vals)
    
    # Action methods
    
    def action_accept(self):
        if self.status == "refused":
            raise exceptions.UserError("Refused offers cannot be accepted.")
        if self.property_id.state == "sold":
            raise exceptions.UserError("Can't sell the same house twice")

        self.property_id.state = "offer_accepted"        
        self.property_id.buyer_id = self.partner_id
        self.property_id.selling_price = self.price

        self.status = "accepted"
        
        
        
        return True
    
    def action_refuse(self):
        if self.status == "accepted":
            raise exceptions.UserError("Accepted offers cannot be refused.")
        self.status = "refused"
        return True