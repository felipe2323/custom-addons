# -*- coding: utf-8 -*-
{
    'name': "invoice_sendbill",

    'summary': """
        Este modulo agrega checkboxe en account_invoice
        Facturas enviadas: Cliente / Asesorm""",

    'description': """
        Facturas enviadas: Cliente / Asesor
    """,

    'author': "Ana Iris Castro Ramirez",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Customer',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account', 'sb_quotation_changes'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}