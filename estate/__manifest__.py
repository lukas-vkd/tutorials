{
    'name': "Real Estate",
    'version': '17.0.1.25.2',
    'license': 'OPL-1',
    'author': "VK DATA ApS",
    'depends': ['base'],
    'summary': 'A module designed to list real estate and it\'s properties',
    'category': 'Sales',
    'description': 'The Real Estate module provides tools to list Estate properties, like the price, features and availability of the properties',
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_type_views.xml',
        'views/res_users_views.xml',
        'views/estate_menus.xml',
    ]

}