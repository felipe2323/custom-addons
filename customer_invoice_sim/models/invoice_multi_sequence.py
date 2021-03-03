from odoo import  fields, models, api, _

class InvoiceMultiSequence(models.Model):
    _name = 'invoice.multi.sequence'
    
    name = fields.Char("Name")
    squence_id = fields.Many2one('ir.sequence',string="Sequence")
    
