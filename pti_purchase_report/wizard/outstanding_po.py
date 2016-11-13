import pytz
import logging
import time
from datetime import datetime, timedelta
from openerp import models, fields, api, _
from openerp.exceptions import UserError
import re
import base64
import cStringIO
import xlsxwriter
from cStringIO import StringIO

_logger = logging.getLogger(__name__)

class EFaktur(models.TransientModel):
    _name = 'outstanding.purchase.information'

    data_x   = fields.Binary(string="File", readonly=True)
    name     = fields.Char('Filename',size=100, readonly=True)
    state_x  = fields.Selection((('choose','choose'),('get','get'),), default='choose')

    @api.multi     
    def outstanding_po_report(self):
        sql = '''
            QUERY
        '''
        self.env.cr.execute(sql)
        outstanding_po = self.env.cr.fetchall()
        
        fp = StringIO()
        workbook = xlsxwriter.Workbook(fp)
        filename = 'Outstanding PO.xlsx'
        
        #### STYLE
        #################################################################################
        top_style = workbook.add_format({'bold': 1,'valign':'vcenter','align':'center'})
        top_style.set_font_name('Arial')
        top_style.set_font_size('15')
        top_style.set_text_wrap()
        #################################################################################
        header_style = workbook.add_format({'bold': 1,'align':'center','valign':'vcenter'})
        header_style.set_font_name('Arial')
        header_style.set_font_size('11')
        header_style.set_border()
        header_style.set_text_wrap()
        header_style.set_bg_color('#BDC3C7')
        #################################################################################
        normal_style = workbook.add_format({'valign':'vcenter'})
        normal_style.set_border()
        normal_style.set_text_wrap()
        normal_style.set_font_name('Arial')
        normal_style.set_font_size('11')
        #################################################################################
        normal_center = workbook.add_format({'valign':'vcenter','align':'center'})
        normal_center.set_border()
        normal_center.set_text_wrap()
        normal_center.set_font_name('Arial')
        normal_center.set_font_size('11')
        #################################################################################
        normal_float = workbook.add_format({'valign':'vcenter'})
        normal_float.set_border()
        normal_float.set_text_wrap()
        normal_float.set_num_format('#,##0.00;-#,##0.00')
        normal_float.set_font_name('Arial')
        normal_float.set_font_size('11')
        #################################################################################
        
        worksheet = workbook.add_worksheet("Schedule Payment")
        worksheet.set_column('A:A', 10) 
        worksheet.set_column('B:B', 8) 
        worksheet.set_column('C:C', 60)
        worksheet.set_column('D:D', 5)
        worksheet.set_column('E:E', 8)
        worksheet.set_column('F:G', 20)      
        
        worksheet.merge_range('A1:F1', 'Outstanding purchase order', top_style)        
        
        worksheet.set_row(0, 30)
        worksheet.set_row(2, 25)
        worksheet.write(2,0, 'Vendor', header_style)
        worksheet.write(2,1, 'PO', header_style)
        worksheet.write(2,2, 'Product', header_style)
        worksheet.write(2,3, 'Total', header_style)
        worksheet.write(2,4, 'UoM', header_style)
        worksheet.write(2,5, 'Schedule Date', header_style)
        
        row = 3
        vendor = False
        po = False
        for data in outstanding_po:
            worksheet.write(row,1, '', normal_style)
            worksheet.write(row,2, data[4], normal_style)
            worksheet.write(row,3, data[2], normal_style)
            worksheet.write(row,4, data[3], normal_style)
            worksheet.write(row,5, data[5], normal_style)
            row += 1

        workbook.close()
        out=base64.encodestring(fp.getvalue())
        self.write({'state_x':'get', 'data_x':out, 'name': filename})
        ir_model_data = self.pool.get('ir.model.data')
        fp.close()
        
        form_res = ir_model_data.get_object_reference(self._cr,self._uid, 'pti_purchase_report', 'outstanding_po_view')
        form_id = form_res and form_res[1] or False
        return {
            'name': _('Download XLS'),
             'view_type': 'form',
             'view_mode': 'form',
             'res_model': 'outstanding.purchase.information',
             'res_id': self.id,
             'view_id': False,
             'views': [(form_id, 'form')],
             'type': 'ir.actions.act_window',
             'target': 'current'
         }
