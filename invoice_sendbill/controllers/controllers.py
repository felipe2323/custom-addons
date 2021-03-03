# -*- coding: utf-8 -*-
from odoo import http

# class InvoiceSendbill(http.Controller):
#     @http.route('/invoice_sendbill/invoice_sendbill/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/invoice_sendbill/invoice_sendbill/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('invoice_sendbill.listing', {
#             'root': '/invoice_sendbill/invoice_sendbill',
#             'objects': http.request.env['invoice_sendbill.invoice_sendbill'].search([]),
#         })

#     @http.route('/invoice_sendbill/invoice_sendbill/objects/<model("invoice_sendbill.invoice_sendbill"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('invoice_sendbill.object', {
#             'object': obj
#         })