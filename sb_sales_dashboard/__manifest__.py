# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

#-*- coding:utf-8 -*-
##############################################################################
#
#    SnippetBucket, MidSized Business Application Solution
#    Copyright (C) 2013-2014 http://snippetbucket.com/. All Rights Reserved.
#    Email: snippetbucket@gmail.com, Skype: live.snippetbucket
#
#
##############################################################################
{
    'name': "SB - Sales Dashboard",
    'summary': """SnippetBucket Sales Dashboard.""",
    'description': """

                    Support: business@snipppetbucket.com

                    Powered by: snippetbucket technologies, snippetbucket.com
                   """,
    'depends' : ['sale','surgicalmed_crm_ext'],
    'author': "SnippetBucket",
    'website': "https://snippetbucket.com/",
    'category': 'SnippetBucket',
    'version': '0.1',

    'data': [
            'views.xml',
            'security/groups.xml',
            'security/ir.model.access.csv',
            'data.xml',
            ],

    'demo': [],
    'installable': True,
    'auto_install': False,
    'images': [],
    "license": 'Other proprietary',
}
