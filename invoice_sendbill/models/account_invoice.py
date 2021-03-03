# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class type_type(models.Model):
    _name = 'type.type'

    name = fields.Char(string="Enviar", required=False, )

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    #send_bill_cust_ids = fields.Many2many('type.type', 'type_help_rel', 'type_id', 'help_id', 'Type')
    fcliente = fields.Boolean(string="Cliente")
    fasesor = fields.Boolean(string="Asesor")