from odoo import models, fields, api, _
import json

class purchase_dashboard(models.Model):
    _name="purchase.dashboard"

    color = fields.Integer("Color Index", default=0)
    name = fields.Char(string='Name')
    type_graph = fields.Char(string="Type")
    kanban_dashboard = fields.Text()
    products = fields.Text(string="Products")
    kanban_dashboard_graph = fields.Text(compute='_kanban_dashboard_graph')

    
    @api.one
    def _kanban_dashboard_graph(self):

        prod = self.env.ref('sb_purchase_dashboard.sb_purchase_dashboard_1')
        prod.write({"name":_("Top 20 Products")})
        prod.kanban_dashboard_graph = json.dumps(self.get_bar_graph_top_products_datas())

        ven = self.env.ref('sb_purchase_dashboard.sb_purchase_dashboard_2')
        ven.write({"name":_("Top 20 Vendors")})
        ven.kanban_dashboard_graph = json.dumps(self.get_bar_graph_top_vendors_datas())

    @api.multi
    def get_bar_graph_top_products_datas(self):

        data = []
        prod = self.env.ref('sb_purchase_dashboard.sb_purchase_dashboard_1')

        query = '''select (select default_code from product_product where id = line.product_id), sum(product_qty) from purchase_order_line as line group by product_id  order by sum desc OFFSET 0 LIMIT 20;'''
        self.env.cr.execute(query)
        recs = self.env.cr.fetchall()

        j=0
        for i in recs:
            data.append({'label':recs[j][0] , 'value':recs[j][1]})
            j+=1

        return [{'values': data}]


    @api.multi
    def get_bar_graph_top_vendors_datas(self):

        data = []
        ven = self.env.ref('sb_purchase_dashboard.sb_purchase_dashboard_2')

        query = '''select (select name from res_partner where id = line.partner_id), count(id) from purchase_order as line group by partner_id  order by count desc OFFSET 0 LIMIT 20;'''
        self.env.cr.execute(query)
        recs = self.env.cr.fetchall()

        j=0
        for i in recs:
            data.append({'label':recs[j][0] , 'value':recs[j][1]})
            j+=1
        return [{'values': data}]

