from odoo import fields, models, api
from odoo.exceptions import UserError


class SaleOrderLineImport(models.Model):
    _inherit = 'sale.order'

    def import_sale_order(self):
        # print("sddhi")
        print(self.id)
        return {
            'name': 'Import Sale Order Line',
            'domain': [],
            'res_model': 'import.so.wizard',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_type': 'form',
            'context': {},
            'target': 'new',
        }

    def action_merge(self):

        for line in self.order_line:
            if line.id in self.order_line.ids:
                line_ids = self.order_line.filtered(lambda m: m.product_id.id == line.product_id.id)

        quantity = 0
        for qty in line_ids:
            quantity += qty.product_uom_qty
        line_ids[0].write({'product_uom_qty': quantity, 'order_id': line_ids[0].order_id.id})
        line_ids[1:].unlink()
