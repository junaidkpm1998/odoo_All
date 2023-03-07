from odoo import models, fields
import openpyxl
import base64
from io import BytesIO
from odoo.exceptions import UserError


class ImportOrderLine(models.Model):
    _name = "import.so.wizard"

    file = fields.Binary(string="Upload", required=True)

    def import_customer(self):
        try:
            wb = openpyxl.load_workbook(filename=BytesIO(base64.b64decode(self.file)), read_only=True)
            ws = wb.active

            for record in ws.iter_rows(min_row=2, max_row=None, min_col=None, max_col=7, values_only=True):
                if record[0]:
                    serach = self.env['product.product'].search([('name', '=', record[0])])
                    if serach:
                        vals = {
                            'product_template_id': record[0],
                            'product_uom_qty': record[1],
                            'price_unit': serach.lst_price,
                            'product_uom': record[2],
                            'name': serach.default_code,
                            'order_id': self.id,
                            'product_id': serach.id,
                        }
                        current_id = self.env.context.get('active_id')
                        print(current_id)
                        sale = self.env['sale.order'].browse(current_id)
                        sale.update({
                            'order_line': [(0, 0, vals)]})

                    else:
                        new_product = self.env['product.product'].create({
                            'name': record[0],
                            'lst_price': record[4],
                            'default_code': record[3]
                        })
                        vals = {
                            'product_template_id': new_product.name,
                            'product_uom_qty': record[1],
                            'price_unit': new_product.lst_price,
                            'product_uom': record[2],
                            'name': new_product.default_code,
                            'order_id': self.id,
                            'product_id': new_product.id,
                        }
                        current_id = self.env.context.get('active_id')
                        print(current_id)
                        sale = self.env['sale.order'].browse(current_id)
                        sale.update({
                            'order_line': [(0, 0, vals)]})
        except:
            raise UserError(('file not found'))
