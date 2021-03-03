from datetime import datetime, date, time, timedelta
from odoo import models, fields, api, _
import pendulum
import json
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF
from babel.dates import format_datetime, format_date

class sale_dashboard(models.Model):
    _name="sale.dashboard"

    color = fields.Integer("Color Index", default=0)
    name = fields.Char(string='Name')
    type_graph = fields.Char(string="Type")
    kanban_dashboard = fields.Text()
    mon_quot = fields.Text(string="Monthly Quotations")
    quater_quot = fields.Text(string="Quaterly Quotations")
    mon_order = fields.Text(string="Monthly Orders")
    quater_order = fields.Text(string="Quaterly Orders")
    mon_client = fields.Text(string="Monthly New Clients")
    quater_client = fields.Text(string="Quaterly New Clients")
    mon_total_sale = fields.Text(string="Monthly Sale Orders Total")
    quater_total_sale = fields.Text(string="Quaterly Sale Orders Total")
    yearly_total_sale = fields.Text(string="Yearly Sale Orders Total")  
    mon_gross_margin = fields.Text(string="Monthly Gross Margin Of Sales")
    quater_gross_margin = fields.Text(string="Quaterly Gross Margin Of Sales")
    # yearly_gross_margin = fields.Text(string="Yearly Gross Margin Of Sales")
    kanban_dashboard_graph = fields.Text(compute='_kanban_dashboard_graph')


    def action_sale_quotation(self):
        _sale = self.env['sale.order']
        months=0
        curr_month = pendulum.parse(pendulum.today().subtract(months=months).to_date_string()).format('MM')
        curr_year = pendulum.parse(pendulum.today().subtract(months=months).to_date_string()).format('YYYY')
        year = int(curr_year)
        last_4_year = int(year-4)

        monthly_quotes = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
        quaterly_quotes = {1:0,2:0,3:0,4:0}

        monthly_orders = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
        quaterly_orders = {1:0,2:0,3:0,4:0}

        monthly_clients = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
        quaterly_clients = {1:0,2:0,3:0,4:0}

        monthly_total = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
        quaterly_total = {1:0,2:0,3:0,4:0}
        yearly_total = {1:0,2:0,3:0,4:0,5:0}

        monthly_gross_margin = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
        quaterly_gross_margin = {1:0,2:0,3:0,4:0}
        # yearly_gross_margin = {1:0,2:0,3:0,4:0,5:0}


    # TO GET MONTHLY SALE QUOTATIONS
        for i in range(1,13):
            start_time = pendulum.parse(pendulum.datetime(year,i,1).subtract(months=months).to_date_string()).start_of('month').to_date_string()
            end_time = pendulum.parse(pendulum.datetime(year,i,1).subtract(months=months).to_date_string()).end_of('month').to_date_string()
            monthly_quote_count = _sale.search([('date_order', '>=', start_time), ('date_order', '<=', end_time)], count = True)
            monthly_quotes[i] = int(monthly_quote_count)
        quot1 = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_1')
        
        if quot1:
            quot1.mon_quot = False
            quot1.quater_quot = False
            quot1.mon_quot = monthly_quotes


#     TO GET QUATERLY SALE QUOTATIONS
        j=0
        for i in range(1,5):
            start_time = pendulum.parse(pendulum.datetime(year,j+1,1).subtract(months=months).to_date_string()).start_of('month').to_date_string()
            end_time = pendulum.parse(pendulum.datetime(year,j+3,1).subtract(months=months).to_date_string()).end_of('month').to_date_string()
            quaterly_quote_count = _sale.search([('date_order', '>=', start_time), ('date_order', '<=', end_time)], count = True)
            quaterly_quotes[i] = int(quaterly_quote_count)
            j+=3

        quot2 = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_2')
        if quot2:
            quot2.mon_quot = False
            quot2.quater_quot = False
            quot2.quater_quot = quaterly_quotes


    # TO GET MONTHLY SALE ORDERS
        for i in range(1,13):
            start_time = pendulum.parse(pendulum.datetime(year,i,1).subtract(months=months).to_date_string()).start_of('month').to_date_string()
            end_time = pendulum.parse(pendulum.datetime(year,i,1).subtract(months=months).to_date_string()).end_of('month').to_date_string()
            monthly_order_count = _sale.search([('state','in',('sale','done')), ('date_order', '>=', start_time), ('date_order', '<=', end_time)], count = True)
            monthly_orders[i] = int(monthly_order_count)
        ord1 = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_3')
        
        if ord1:
            ord1.mon_quot = False
            ord1.quater_quot = False
            ord1.mon_order = False
            ord1.quater_order = False
            ord1.mon_order = monthly_orders


#     TO GET QUATERLY SALE ORDERS
        j=0
        for i in range(1,5):
            start_time = pendulum.parse(pendulum.datetime(year,j+1,1).subtract(months=months).to_date_string()).start_of('month').to_date_string()
            end_time = pendulum.parse(pendulum.datetime(year,j+3,1).subtract(months=months).to_date_string()).end_of('month').to_date_string()
            quaterly_order_count = _sale.search([('state', 'in', ['sale','done']),  ('date_order', '>=', start_time), ('date_order', '<=', end_time)], count = True)
            quaterly_orders[i] = int(quaterly_order_count)
            j+=3

        ord2 = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_4')
        if ord2:
            ord2.mon_quot = False
            ord2.quater_quot = False
            ord2.mon_order = False
            ord2.quater_order = False
            ord2.quater_order = quaterly_orders


    # TO GET MONTHLY NEW CLIENTS

        for i in range(1,13):
            start_time = pendulum.parse(pendulum.datetime(year,i,1).subtract(months=months).to_date_string()).start_of('month').to_date_string()
            end_time = pendulum.parse(pendulum.datetime(year,i,1).subtract(months=months).to_date_string()).end_of('month').to_date_string()
            monthly_sale_ids = _sale.search([('state','in',('sale','done')), ('date_order', '>=', start_time), ('date_order', '<=', end_time)])
            partner_ids = [ x.partner_id.id for x in monthly_sale_ids if x.partner_id and x.partner_id.id]

            filtered_ids = []
            for x in set(partner_ids):
                so = _sale.search([('state','in',('sale','done')),('date_order', '<', start_time),('partner_id','=',x)],limit=1).ids
                if so == []:
                    filtered_ids.append(x)
            monthly_clients[i] = len(filtered_ids)


        cli1 = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_5')
        if cli1:
            cli1.mon_quot = False
            cli1.quater_quot = False
            cli1.mon_order = False
            cli1.quater_order = False
            cli1.mon_client = False
            cli1.quater_client = False
            cli1.mon_client = monthly_clients


#    TO GET QUATERLY NEW CLIENTS
        j=0
        for i in range(1,5):
            start_time = pendulum.parse(pendulum.datetime(year,j+1,1).subtract(months=months).to_date_string()).start_of('month').to_date_string()
            end_time = pendulum.parse(pendulum.datetime(year,j+3,1).subtract(months=months).to_date_string()).end_of('month').to_date_string()
            quaterly_sale_ids = _sale.search([('state','in',('sale','done')), ('date_order', '>=', start_time), ('date_order', '<=', end_time)])
            quater_partner_ids = [ x.partner_id.id for x in quaterly_sale_ids if x.partner_id and x.partner_id.id]

            quater_filtered_ids = []
            for x in set(quater_partner_ids):
                so = _sale.search([('state','in',('sale','done')),('date_order', '<', start_time),('partner_id','=',x)],limit=1).ids
                if so == []:
                    quater_filtered_ids.append(x)
            quaterly_clients[i] = len(quater_filtered_ids)
            j+=3

        cli2 = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_6')
        
        if cli2:
            cli2.mon_quot = False
            cli2.quater_quot = False
            cli2.mon_order = False
            cli2.quater_order = False
            cli2.mon_client = False
            cli2.quater_client = False
            cli2.quater_client = quaterly_clients


#    TO GET MONTHLY SALE ORDER TOTAL
        for i in range(1,13):
            start_time = pendulum.parse(pendulum.datetime(year,i,1).subtract(months=months).to_date_string()).start_of('month').to_date_string()
            end_time = pendulum.parse(pendulum.datetime(year,i,1).subtract(months=months).to_date_string()).end_of('month').to_date_string()
            monthly_order_total = _sale.search([('state','in',('sale','done')), ('date_order', '>=', start_time), ('date_order', '<=', end_time)])
            total=0
            for x in monthly_order_total:
                total+= x.amount_untaxed
            monthly_total[i] = total
        mon_tot1 = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_7')
        
        if mon_tot1:
            mon_tot1.mon_quot = False
            mon_tot1.quater_quot = False
            mon_tot1.mon_order = False
            mon_tot1.quater_order = False
            mon_tot1.mon_client = False
            mon_tot1.quater_client = False
            mon_tot1.mon_total_sale = monthly_total


#     TO GET QUATERLY SALE ORDERS TOTAL
        j=0
        for i in range(1,5):
            start_time = pendulum.parse(pendulum.datetime(year,j+1,1).subtract(months=months).to_date_string()).start_of('month').to_date_string()
            end_time = pendulum.parse(pendulum.datetime(year,j+3,1).subtract(months=months).to_date_string()).end_of('month').to_date_string()
            quaterly_sale_total = _sale.search([('state','in',['sale','done']), ('date_order', '>=', start_time), ('date_order', '<=', end_time)])
            total=0
            for x in quaterly_sale_total:
                total+= x.amount_untaxed
            quaterly_total[i] = total
            j+=3

        quater_tot1 = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_8')
        if quater_tot1:
            quater_tot1.mon_quot = False
            quater_tot1.quater_quot = False
            quater_tot1.mon_order = False
            quater_tot1.quater_order = False
            quater_tot1.mon_client = False
            quater_tot1.quater_client = False
            quater_tot1.quater_total_sale = quaterly_total


#    TO GET YEARLY SALE ORDERS TOTAL
        j=0
        for i in range(1,6):
            start_time = pendulum.parse(pendulum.datetime(last_4_year+j,1,1).subtract(months=months).to_date_string()).start_of('month').to_date_string()
            end_time = pendulum.parse(pendulum.datetime(last_4_year+j,12,1).subtract(months=months).to_date_string()).end_of('month').to_date_string()
            yearly_order_total = _sale.search([('state','in',('sale','done')), ('date_order', '>=', start_time), ('date_order', '<=', end_time)])
            total=0
            for x in yearly_order_total:
                total+= x.amount_untaxed
            yearly_total[i] = total
            j+=1
        year_tot1 = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_9')
        
        if year_tot1:
            year_tot1.mon_quot = False
            year_tot1.quater_quot = False
            year_tot1.mon_order = False
            year_tot1.quater_order = False
            year_tot1.mon_client = False
            year_tot1.quater_client = False
            year_tot1.yearly_total_sale = yearly_total


#    TO GET MOTHLY GROSS MARGIN ON SALE ORDERS
        gross_mar=0
        k=0
        for i in range(1,13):
            start_time = pendulum.parse(pendulum.datetime(year,i,1).subtract(months=months).to_date_string()).start_of('month').to_date_string()
            end_time = pendulum.parse(pendulum.datetime(year,i,1).subtract(months=months).to_date_string()).end_of('month').to_date_string()
            monthly_sale_order = _sale.search([('state','in',('sale','done')), ('date_order', '>=', start_time), ('date_order', '<=', end_time)])
            total=0
            temp=0
            # count1 = len(monthly_sale_order)
            # print(count1)
            for x in monthly_sale_order:
                # print('[[[[[[[[[[[[[[',x)
                a=0
                k+=1
                gross=0
                for y in x.order_line:
                    if y.gross_margin:
                        a+=1
                        z= y.gross_margin
                        gross+=z
                        # print('@@@@@@',z)
                        # print('#########',gross)
                if a>0:
                    total = gross/a
                    temp+=total
                    # print('$$$$$$$$$$$$$',total,a)
            # print('<<<<<<<<<<<<<<<<<<<<',temp)
            # print('/////////////////////////////',k)
            if temp>0:
                gross_mar=temp/k
                # print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',gross_mar)
            monthly_gross_margin[i] = gross_mar
            gross_mar=0
            k=0
            # print('=======================================================================================================')
        mon_gross_mar = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_10')
        
        if mon_gross_mar:
            mon_gross_mar.mon_quot = False
            mon_gross_mar.quater_quot = False
            mon_gross_mar.mon_order = False
            mon_gross_mar.quater_order = False
            mon_gross_mar.mon_client = False
            mon_gross_mar.quater_client = False
            mon_gross_mar.mon_total_sale = False
            mon_gross_mar.quater_total_sale = False
            mon_gross_mar.yearly_total_sale = False
            mon_gross_mar.mon_gross_margin = monthly_gross_margin


#    TO GET QUATERLY GROSS MARGIN ON SALES
        # gross_mar=0
        # k=0
        # j=0
        # for i in range(1,5):
        #     start_time = pendulum.parse(pendulum.datetime(year,j+1,1).subtract(months=months).to_date_string()).start_of('month').to_date_string()
        #     end_time = pendulum.parse(pendulum.datetime(year,j+3,1).subtract(months=months).to_date_string()).end_of('month').to_date_string()
        #     quaterly_sale_order = _sale.search([('state','in',['sale','done']), ('date_order', '>=', start_time), ('date_order', '<=', end_time)])
        #     total=0
        #     temp=0
        #     # b=0
        #     # count = len(quaterly_sale_order)
        #     # print(count,'??????????????????????????????????????')
        #     for x in quaterly_sale_order:
        #         print('##########',x)
        #         a=0
        #         k+=1
        #         gross=0
        #         for y in x.order_line:
        #             if y.gross_margin:
        #                 a+=1
        #                 z= y.gross_margin
        #                 gross+=z
        #                 print('<<<<<<<<<<<<<',z)
        #                 print('@@@@@@@@@@@@@@@@@',gross)
                
        #         if a>0:
                 
        #             total = gross/a
        #             temp+=total
        #             print('$$$$$$$$$$$$$$$$$$$$$$$$$$$',total,a)
        #             # b+=a
        #             # print(b)
        #     if temp>0:
        #         # print(b)
        #         # print(k,'////////////////')
        #         # print(temp1)
        #         gross_mar=temp/k
        #         print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&,',gross_mar)
        #     print('=======================================================================================================')
        #     quaterly_gross_margin[i] = gross_mar
        #     gross_mar=0
        #     k=0
        #     j+=3

        gross_mar=0
        k=0
        counter=0
        quater_gross=0
        m=1
        for i in range(1,13):
            start_time = pendulum.parse(pendulum.datetime(year,i,1).subtract(months=months).to_date_string()).start_of('month').to_date_string()
            end_time = pendulum.parse(pendulum.datetime(year,i,1).subtract(months=months).to_date_string()).end_of('month').to_date_string()
            quaterly_sale_order = _sale.search([('state','in',('sale','done')), ('date_order', '>=', start_time), ('date_order', '<=', end_time)])
            counter+=1
            total=0
            temp=0
            count1 = len(quaterly_sale_order)
            # print(count1)
            for x in quaterly_sale_order:
                # print('[[[[[[[[[[[[[[',x)
                a=0
                k+=1
                gross=0
                for y in x.order_line:
                    if y.gross_margin:
                        a+=1
                        z= y.gross_margin
                        gross+=z
                        # print('@@@@@@',z)
                        # print('#########',gross)
                if a>0:
                    total = gross/a
                    temp+=total
            #         print('$$$$$$$$$$$$$',total,a)
            # print('<<<<<<<<<<<<<<<<<<<<',temp)
            # print('/////////////////////////////',k)
            if temp>0:
                gross_mar=temp/k
                if counter<=3:
                    quater_gross+=gross_mar
                    # print('aaaaaaaaaaaa',gross_mar)
                    # print('bbbbbbbbbbbbbbbbbb',quater_gross)

                    if counter==3:
                        # print(m)
                        quaterly_gross_margin[m] = quater_gross/3    
                        m+=1
                        # print('ccccccccccccccccccccccccccccccccc',quater_gross/3)
                        counter=0
                        quater_gross=0        
                    
                
                
            gross_mar=0
            k=0
            # print('=======================================================================================================')

        quater_gross_mar = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_11')
        if quater_gross_mar:
            quater_gross_mar.mon_quot = False
            quater_gross_mar.quater_quot = False
            quater_gross_mar.mon_order = False
            quater_gross_mar.quater_order = False
            quater_gross_mar.mon_client = False
            quater_gross_mar.quater_client = False
            quater_gross_mar.mon_total_sale = False
            quater_gross_mar.quater_total_sale = False
            quater_gross_mar.yearly_total_sale = False
            quater_gross_mar.quater_gross_margin = quaterly_gross_margin

    @api.one
    def _kanban_dashboard_graph(self):

        quot12 = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_1')
        quot12.write({"name":_("Monthly Quotations")})
        quot22 = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_2')
        quot22.write({"name":_("Quaterly Quotations")})
        quot12.kanban_dashboard_graph = json.dumps(self.get_bar_graph_monthly_datas())
        quot22.kanban_dashboard_graph = json.dumps(self.get_bar_graph_quaterly_datas())

        ord1 = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_3')
        ord1.name=_("Monthly Sales Orders")
        ord2 = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_4')
        ord2.name=_("Quaterly Sales Orders")
        ord1.kanban_dashboard_graph = json.dumps(self.get_bar_graph_monthly_order_datas())
        ord2.kanban_dashboard_graph = json.dumps(self.get_bar_graph_quaterly_order_datas())


        cli1 = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_5')
        cli1.name=_("Monthly New Clients")
        cli2 = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_6')
        cli2.name=_("Quaterly New Clients")
        cli1.kanban_dashboard_graph = json.dumps(self.get_bar_graph_monthly_client_datas())
        cli2.kanban_dashboard_graph = json.dumps(self.get_bar_graph_quaterly_client_datas())

        mon_tot1 = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_7')
        mon_tot1.name=_("Monthly Sale Order Total")
        quater_tot1 = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_8')
        quater_tot1.name=_("Quaterly Sale Order Total")
        year_tot1 = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_9')
        year_tot1.name=_("Yearly Sale Order Total")
        mon_tot1.kanban_dashboard_graph = json.dumps(self.get_bar_graph_monthly_sale_total_datas())
        quater_tot1.kanban_dashboard_graph = json.dumps(self.get_bar_graph_quaterly_sale_total_datas())
        year_tot1.kanban_dashboard_graph = json.dumps(self.get_bar_graph_yearly_sale_total_datas())

        mon_gross_mar = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_10')
        mon_gross_mar.name=_("Monthly Gross Margin")
        quater_gross_mar = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_11')
        quater_gross_mar.name=_("Quaterly Gross Margin")
        mon_gross_mar.kanban_dashboard_graph = json.dumps(self.get_bar_graph_monthly_gross_margin_datas())
        quater_gross_mar.kanban_dashboard_graph = json.dumps(self.get_bar_graph_quaterly_gross_margin_datas())


    @api.multi
    def get_bar_graph_monthly_datas(self):
        data = []
        quot12 = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_1')

        month_names = [_("Jan"),_("Feb"),_("Mar"),_("Apr"),_("May"),_("Jun"),_("Jul"),_("Aug"),_("Sep"),_("Oct"),_("Nov"),_("Dec")]
        dict1 = eval(quot12.mon_quot)
        for i in range(0,12):
                data.append({'label': month_names[i], 'value':dict1[i+1]})

        return [{'values': data}]



    @api.multi
    def get_bar_graph_quaterly_datas(self):
        data = []
        quot22 = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_2')
        quater_names = [_("Jan-Mar"),_("Apr-Jun"),_("Jul-Sep"),_("Oct-Dec")]
        dict2 = eval(quot22.quater_quot)
        for i in range(0,4):
            data.append({'label': quater_names[i], 'value':dict2[i+1]})

        return [{'values': data}]


    @api.multi
    def get_bar_graph_monthly_order_datas(self):
        data = []
        ord1 = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_3')
        ord2 = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_4')

        month_names = [_("Jan"),_("Feb"),_("Mar"),_("Apr"),_("May"),_("Jun"),_("Jul"),_("Aug"),_("Sep"),_("Oct"),_("Nov"),_("Dec")]
        dict1 = eval(ord1.mon_order)
        for i in range(0,12):
                data.append({'label': month_names[i], 'value':dict1[i+1]})

        return [{'values': data}]



    @api.multi
    def get_bar_graph_quaterly_order_datas(self):
        data = []
        ord2 = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_4')
        quater_names = [_("Jan-Mar"),_("Apr-Jun"),_("Jul-Sep"),_("Oct-Dec")]
        dict2 = eval(ord2.quater_order)
        for i in range(0,4):
            data.append({'label': quater_names[i], 'value':dict2[i+1]})

        return [{'values': data}]


    @api.multi
    def get_bar_graph_monthly_client_datas(self):
        data = []
        cli1 = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_5')

        month_names = [_("Jan"),_("Feb"),_("Mar"),_("Apr"),_("May"),_("Jun"),_("Jul"),_("Aug"),_("Sep"),_("Oct"),_("Nov"),_("Dec")]
        dict1 = eval(cli1.mon_client)
        for i in range(0,12):
                data.append({'label': month_names[i], 'value':dict1[i+1]})

        return [{'values': data}]

    @api.multi
    def get_bar_graph_quaterly_client_datas(self):
        data = []
        cli2 = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_6')
        quater_names = [_("Jan-Mar"),_("Apr-Jun"),_("Jul-Sep"),_("Oct-Dec")]
        dict2 = eval(cli2.quater_client)
        for i in range(0,4):
            data.append({'label': quater_names[i], 'value':dict2[i+1]})

        return [{'values': data}]

    @api.multi
    def get_bar_graph_monthly_sale_total_datas(self):
        data = []
        mon_tot1 = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_7')

        month_names = [_("Jan"),_("Feb"),_("Mar"),_("Apr"),_("May"),_("Jun"),_("Jul"),_("Aug"),_("Sep"),_("Oct"),_("Nov"),_("Dec")]
        dict1 = eval(mon_tot1.mon_total_sale)
        for i in range(0,12):
                data.append({'label': month_names[i], 'value':dict1[i+1]})

        return [{'values': data}]


    @api.multi
    def get_bar_graph_quaterly_sale_total_datas(self):
        data = []
        quater_tot1 = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_8')
        quater_names = [_("Jan-Mar"),_("Apr-Jun"),_("Jul-Sep"),_("Oct-Dec")]
        dict2 = eval(quater_tot1.quater_total_sale)
        for i in range(0,4):
            data.append({'label': quater_names[i], 'value':dict2[i+1]})

        return [{'values': data}]

    @api.multi
    def get_bar_graph_yearly_sale_total_datas(self):
        data = []
        year_tot1 = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_9')

        months=0
        curr_year = pendulum.parse(pendulum.today().subtract(months=months).to_date_string()).format('YYYY')
        year = int(curr_year)
        last_4_year = year-4

        years = [last_4_year,last_4_year+1,last_4_year+2,last_4_year+3,last_4_year+4]
        dict2 = eval(year_tot1.yearly_total_sale)
        for i in range(0,5):
            data.append({'label': years[i], 'value':dict2[i+1]})

        return [{'values': data}]


    @api.multi
    def get_bar_graph_monthly_gross_margin_datas(self):
        data = []
        mon_gross_mar = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_10')

        month_names = [_("Jan"),_("Feb"),_("Mar"),_("Apr"),_("May"),_("Jun"),_("Jul"),_("Aug"),_("Sep"),_("Oct"),_("Nov"),_("Dec")]
        dict1 = eval(mon_gross_mar.mon_gross_margin)
        for i in range(0,12):
                data.append({'label': month_names[i], 'value':dict1[i+1]})

        return [{'values': data}]

    @api.multi
    def get_bar_graph_quaterly_gross_margin_datas(self):
        data = []
        quater_gross_mar = self.env.ref('sb_sales_dashboard.sb_sales_dashboard_11')
        quater_names = [_("Jan-Mar"),_("Apr-Jun"),_("Jul-Sep"),_("Oct-Dec")]
        dict2 = eval(quater_gross_mar.quater_gross_margin)
        for i in range(0,4):
            data.append({'label': quater_names[i], 'value':dict2[i+1]})

        return [{'values': data}]



