# -*- coding: utf-8 -*-
{
    'name': "Awesome Clicker",

    'summary': """
        Starting module for "Master the Odoo web framework, chapter 1: Build a Clicker game"
    """,

    'description': """
        Starting module for "Master the Odoo web framework, chapter 1: Build a Clicker game"
    """,

    'author': "Odoo",
    'website': "https://www.odoo.com/",
    'category': 'Tutorials/AwesomeClicker',
    'version': '17.0.0.7.0',
    'application': True,
    'installable': True,
    'depends': ['base', 'web'],

    'data': [],
    'assets': {
        'web.assets_backend': [
            'awesome_clicker/static/src/**/*',
        ],

    },
    'license': 'AGPL-3'
}
