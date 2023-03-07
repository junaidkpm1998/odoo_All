from odoo import models, fields, _
import openpyxl
import base64
from io import BytesIO
from odoo.exceptions import UserError


class ImportCustomerWizard(models.TransientModel):
    _name = "import.so.wizard"
    file = fields.Binary(string="File", required=True)

    sale_order_id = fields.Many2one('sale.order')

    def import_customer(self):
        print("vmbvmbb")
        print(self.sale_order_id)

        # try:
        wb = openpyxl.load_workbook(

            filename=BytesIO(base64.b64decode(self.file)), read_only=True
        )
        ws = wb.active
        for record in ws.iter_rows(min_row=2, max_row=None, min_col=None, max_col=None, values_only=True):

            search = self.env['product.product'].search([
                ('name', '=', record[0])])
            # product_id = self.env['product.product'].id

            # print(search)
            if not search:
                self.env['sale.order.line'].create({
                    'product_id': search.id,
                    'product_template_id': record[0],
                    'product_uom_qty': record[1],
                    'product_uom': record[2],
                    'name': record[3],
                    'price_unit': record[4],
                    'order_id': self.sale_order_id.id,
                })
                print(record[0])

            # except:
            # raise UserError(
            #     _('Please insert a valid file'))
