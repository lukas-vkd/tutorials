from dateutil.relativedelta import relativedelta

from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "represents a property listed on the module"
    name = fields.Char('Title', required=True)
    description = fields.Text("Description")
    postcode = fields.Char("Postcode")
    # the default date_availability should be 3 months from the current time
    date_availability = fields.Date("Available From", copy=False, default=fields.Date.add(fields.Date.today() + relativedelta(months =+ 3)))
    expected_price = fields.Float("Expected Price", required=True)
    selling_price = fields.Float("Selling Price", readonly= True, copy=False)
    bedrooms = fields.Integer("Bedrooms", default="2")
    living_area = fields.Integer("Living Area (sqm)")
    facades = fields.Integer("Facades")
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer("Garden Area (sqm)")
    garden_orientation = fields.Selection(
        string='Direction',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="Type is used to describe which way the garden is pointing")
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string='State',
        selection=[('new', 'New'), ('offer Received', 'Offer Received'), ('offer Accepted', 'Offer Accepted'), ('sold ', 'Sold'), ('canceled ', 'Canceled')],
        help="Type is used to describe the state of the property",
        default='new')
