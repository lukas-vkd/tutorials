{
    'name': "Real Estate",
    'version': '17.0.1.26.0',
    'license': 'OPL-1',
    'author': "VK DATA ApS",
    'depends': ['base'],
    'summary': 'A module designed to list real estate and it\'s properties',
    'category': 'Real Estate/Brokerage',
    'description': 'The Real Estate module provides tools to list Estate properties, like the price, features and availability of the properties',
    'application': True,
    'data': [
        'views/estate_property_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_type_views.xml',
        'views/res_users_views.xml',
        'views/estate_menus.xml',

        'security/estate_groups.xml',
        'security/ir.model.access.csv',
        'security/estate_property_security.xml',

    ]

}