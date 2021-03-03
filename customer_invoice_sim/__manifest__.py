# -*- coding: utf-8 -*-
{
    'name': "SIM - Account invoice Extention",
    'summary': """SIM - Account invoice Extention""",
    'description':"",
    'depends' : ['account','surgicalmed_crm_ext'],
    'author': "Nilesh Sheliya",
    'website':'',
    'version': '1.0',

    'data': [
            'security/ir.model.access.csv',
            'views/customer_invoice_extends.xml',
            'views/invoice_multi_sequence.xml',
             ],

    'demo': [],
    'installable': True,
    'auto_install': False,
    'images': [],
}
