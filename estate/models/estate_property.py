from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "represents a property listed on the module"

    name = fields.Char('Property Name', required=True)
    description = fields.Text("Property Description")
    postcode = fields.Char("Property Postcode")
    date_availability = fields.Date("")
    expected_price = fields.Float("Expected price to buy the property", required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Direction',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        Help="Type is used to describe which way the garden is pointing")
