from odoo import  fields, models, api
from datetime import datetime

class sale_order(models.Model):
    _inherit="sale.order"

    purchase_order_id = fields.Many2one('purchase.order',string="Purchase Order Id")

    @api.one
    def update_purchase_order(self):
		if self.purchase_order_id:
			self.purchase_order_id.order_line.unlink()
			self.purchase_order_id.write({
						'sale_order_id':self.id,
	 					# 'partner_id':self.supplier_id.id,
	 					# 'currency_id':self.supplier_id.currency_id.id,
	 					# 'date_order':fields.datetime.now(),
	 					# 'date_planned': fields.datetime.now(),
	 					'order_line':[(0, 0,
	 	                                {"product_id": x.product_id.id,
	 	                                 "name": x.name,
	 	                                 "manufacture_code_spt": x.product_id.manufacture_code_spt,
	 	                                 "date_planned": fields.datetime.now(),
	 	                                 "lot_spt": x.lot_spt.id,
	 	                                 "product_qty": x.product_uom_qty,
	 	                                 # "qty_received": x.product_uom_qty,
	 	                                 # "qty_invoiced": x.product_uom_qty,
	 	                                 "product_uom":x.product_uom.id,
	 	                                 "price_unit": x.product_id.standard_price,
	 	                                 # "discount_in_per": 0.00,
	 	                                 # "taxes_id": x.tax_id.id,
	 	                                 "price_subtotal": x.price_subtotal,
	 	                                })for x in self.order_line],
						
	 			})


class sb_purchase_wizard(models.TransientModel):
	_name="sb.purchase.wizard"


	supplier_id = fields.Many2one('res.partner',string="Select Supplier",domain=[('supplier','=',True)])
	order_id = fields.Char(string="Sale Order ID")

	@api.one
	def get_supplier_details(self):

		sorder_id = int(self.order_id)
		purchase_order_ids = self.env['purchase.order'].search([('state','=','draft')])
		sale_order_id = self.env['sale.order'].search([('id', '=', sorder_id)])
		if not sale_order_id.purchase_order_id:
			pur_obj = self.env['purchase.order']
	 		new_purchase_order_id = pur_obj.create({
	 					'sale_order_id':sale_order_id.id,
	 					'partner_id':self.supplier_id.id,
	 					'currency_id':self.supplier_id.currency_id.id,
	 					'date_order':fields.datetime.now(),
	 					# 'date_planned': fields.datetime.now(),
	 					'order_line':[(0, 0,
	 	                                {"product_id": x.product_id.id,
	 	                                 "name": x.name,
	 	                                 "manufacture_code_spt": x.product_id.manufacture_code_spt,
	 	                                 "date_planned": fields.datetime.now(),
	 	                                 "lot_spt": x.lot_spt.id,
	 	                                 "product_qty": x.product_uom_qty,
	 	                                 # "qty_received": x.product_uom_qty,
	 	                                 # "qty_invoiced": x.product_uom_qty,
	 	                                 "product_uom":x.product_uom.id,
	 	                                 "price_unit": x.product_id.standard_price,
	 	                                 # "discount_in_per": 0.00,
	 	                                 # "taxes_id": x.tax_id.id,
	 	                                 "price_subtotal": x.price_subtotal,
	 	                                })for x in sale_order_id.order_line],
						
	 			})
			sale_order_id.purchase_order_id = new_purchase_order_id
			