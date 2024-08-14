from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError
from odoo.tests import tagged
from odoo.fields import Command


@tagged('post_install', '-at_install')
class EstateTestCase(TransactionCase):

    @classmethod
    def setUpClass(cls):
        # add env on cls and many other things
        super(EstateTestCase, cls).setUpClass()

        # create the data for each tests. By doing it in the setUpClass instead
        # of in a setUp or in each test case, we reduce the testing time and
        # the duplication of code.
        cls.properties = cls.env['estate.property'].create(
            {
            'name': 'a basic house',
            'description':'just a house really',
            'postcode':'1234',
            #'date_availability':'',
            'expected_price':'123123',
            #'selling_price':'',
            'bedrooms':'4',
            'living_area':'10',
            'facades':'4',
            'garage':'True',
            'garden':'True',
            'garden_area':'10',
            'total_area':'20',
            #'best_price':'',
            'garden_orientation':'north',
            'active':'True',
            'state':'new',

            #'offer_ids': [
            #    (Command.CREATE, 0, {
            #        'partner_id':'9',
            #        'price':100000
            #    })
            #]
            #'property_type_id':'Test Partner',
            #'sales_person_id':'Test Partner',
            #'buyer_id':'Test Partner',
            #'tag_ids':'Test Partner',

        })
        
        cls.offer = cls.env['estate.property.offer'].create([
           { 
            'property_id': cls.properties.id,
            'price': 100000,
            'partner_id': 9
        
        }])
        print(" reached ".center(100, '='))

        print(cls.properties.id)
        print(cls.offer.property_id)
        print(cls.offer.price)
        print(" reached ".center(100, '='))



    def test_creation_area(self):
        """Test that the total_area is computed like it should."""
        self.properties.living_area = 20
        self.assertRecordValues(self.properties, [{
            'name': 'a basic house',
            'total_area': 30
            }
            

        ])


    def test_action_sell(self):
        """Test that everything behaves like it should when selling a property."""
        self.properties.offer_ids

        self.properties.action_sold()
        self.assertRecordValues(self.properties, [
           {'name': 'a basic house', 'state': 'sold'},
        ])
        
        with self.assertRaises(UserError):
            self.properties.action_sold()
            
    def test_action_sell_on_property_with_no_offers(self):
        """Test that everything behaves like it should when selling a property."""
        self.properties.offer_ids.unlink()
        self.properties.state = "new"

        
        with self.assertRaises(UserError):
            self.properties.action_sold()