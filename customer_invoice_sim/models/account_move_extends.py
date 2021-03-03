from odoo import  fields, models, api, _

class AccountMoveExtends(models.Model):
    _inherit = 'account.move'
    
    @api.multi 
    def post(self):
        res = super(AccountMoveExtends,self).post()
        invoice = self._context.get('invoice', False)
        if invoice:
            if invoice.sequence_type:
                new_name = invoice.sequence_type.squence_id.with_context(ir_sequence_date=self.date).next_by_id()
                self.write({'name':new_name})
        return res
        
