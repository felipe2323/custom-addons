from odoo import  fields, models, api, _
import csv
import logging
import xlsxwriter 
from odoo.exceptions import UserError, ValidationError
logger = logging.getLogger(__name__)
class CustomerInvoiceExtends(models.Model):
    _inherit = 'account.invoice'
    
    customer_type_id = fields.Many2one('res.partner.type',related='partner_id.customer_type_id',string="Customer type",store=True)
    customer_group_id = fields.Many2one('res.partner.group',related='partner_id.group_id',string="Customer Group",store=True)    
    sequence_type = fields.Many2one('invoice.multi.sequence','Sequence Type')
    
    @api.onchange('partner_id')
    def onchange_partner_id(self):
        if self.type == "out_invoice":
            comment = self.env.user.company_id.sale_note or ''
            if self.partner_id.comment:
                if comment:
                    comment += "\n %s" %(self.partner_id.comment)
                else:
                    comment = (self.partner_id.comment)
            self.comment = comment
            
    @api.multi
    def unlink(self):
        for record in self:
            if record.number and record.state not in ('draft','cancel'):
                raise UserError(_('You can not delete invoice'))
        return super(CustomerInvoiceExtends, self).unlink()    
    
    @api.multi
    def action_change_number(self):
        already_invoice =[]   
        old_invoice_number=['2019/00273']
        new_invoice_number=['2019/00253']
        count=0;
        for record in old_invoice_number:
            invoice_to_modify = self.env['account.invoice'].search([('number', '=', record)],limit=1)
            if invoice_to_modify:
                invoice_already_exists = self.env['account.invoice'].search([('number', '=', new_invoice_number[count])])
                if not invoice_already_exists:
                    invoice_to_modify.write({'number':new_invoice_number[count]})
                    invoice_to_modify.move_id.write({'name':new_invoice_number[count]})
                else:
                    invoice_to_store={'number':invoice_already_exists.number}
                    already_invoice.append(invoice_to_store)
            count=count+1
        print already_invoice
        workbook = xlsxwriter.Workbook('customer_invoice.xlsx')     
        worksheet = workbook.add_worksheet() 
        row = 0
        column = 0
        for item in already_invoice : 
            worksheet.write(row, column, item.get('number')) 
            row += 1
        workbook.close()   
    
