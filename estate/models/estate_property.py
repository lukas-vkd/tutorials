from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, exceptions

class EstateProperty(models.Model):
    # fields and methods are chronologicaly ordered to make it easier to follow the tutorial 
    _name = "estate.property"
    _description = "represents a property listed on the module"
    name = fields.Char("Title", required=True)
    description = fields.Text("Description")
    postcode = fields.Char("Postcode")
    # the default date_availability should be 3 months from the current time
    #TODO: make this mode odoo like, it dosen't feel right to use dateutil here
    date_availability = fields.Date("Available From", copy=False, default=fields.Date.add(fields.Date.today() + relativedelta(months =+ 3)))
    expected_price = fields.Float("Expected Price", required=True)
    selling_price = fields.Float("Selling Price", readonly= True, copy=False)
    bedrooms = fields.Integer("Bedrooms", default="2")
    living_area = fields.Integer("Living Area (sqm)")
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Garden")
    garden_area = fields.Integer("Garden Area (sqm)")
    garden_orientation = fields.Selection(
        string="Direction",
        selection=[("north", "North"), ("south", "South"), ("east", "East"), ("west", "West")],
        help="Type is used to describe which way the garden is pointing")
    active = fields.Boolean(default=True)

    state = fields.Selection(
        selection=[
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        string="Status",
        required=True,
        copy=False,
        default="new",
    )

    
    #
    # relationships ≽^•⩊•^≼
    #
    
    property_type_id = fields.Many2one("estate.property.type", string="type" )
    
    # we use the current user's id as the sales_person's id since the user who is listing the property is the seller
    sales_person_id = fields.Many2one("res.users", string="Salesman", default=lambda self: self.env.user)
    #TODO: make a decision on how to handle to buyer when the sale is done 
    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    
    tag_ids = fields.Many2many("estate.property.tag", string="tags")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")
    
    total_area = fields.Integer(compute="_compute_total_area")
    
    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    best_price = fields.Float(compute="_compute_best_price")
    
    #TODO: make this more elegant by using mapped
    @api.depends("offer_ids")
    def _compute_best_price(self):
        for record in self:
            current_best_price = 0
            for offer in record.offer_ids:
                if offer.price > current_best_price:
                    current_best_price = offer.price
            record.best_price = current_best_price

    @api.onchange("garden")
    def _onchange_garden(self):
        self.garden_area = 0
        self.garden_orientation = ""
        if self.garden == True:
            self.garden_area = 10
            self.garden_orientation = "north"
                    
    
    def action_set_sold(self):
        if self.state == "canceled":
            raise exceptions.UserError("Canceled properties cannot be sold.")
        self.state = "canceled"
        return True
    
    def action_set_cancel(self):
        if self.state == "sold":
            raise exceptions.UserError("Sold properties cannot be canceled.")
        self.state = "canceled"
        return True