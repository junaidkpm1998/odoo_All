from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    package = fields.Many2many("package.model", )
    width = fields.Float()

    height = fields.Float()
    length = fields.Float()
    maximum_weight = fields.Float()
    package_field = fields.Char()
    sale_model_values_id = fields.One2many("package.model", 'package_model_id')
    # package_field = fields.Char('package field')
    delivery_done = fields.Boolean('Delivery Done', default=False)
    package_count = fields.Integer(compute='compute_count')


    # @api.depends("partner_id")
    def compute_count(self):
        for record in self:
            record.package_count = self.env['bundle.model'].search_count(
                [('partner_id', '=', self.partner_id.id)])
    @api.onchange('package')
    def sale_package_onchange(self):
        for rec in self.package:
            temp_save = {'width': rec.width, 'height': rec.height, 'length': rec.length,
                         'maximum_weight': rec.maximum_weight, 'package_model_id': rec.id}
            self.write({'sale_model_values_id': [(0, 0, temp_save)]})

    def action_confirm(self):
        value = super(SaleOrder, self).action_confirm()
        # sale_order = self.env['sale.order'].search([])[0]
        # sequence_number = sale_order.name
        # partner = sale_order.partner_id.name
        # exp = sale_order.expected_date
        # print(exp)
        # print(partner)
        # print(sequence_number)
        # print(fields.date.today())
        # print(self.order_line.package_field_id.width)
        bundle = self.env['bundle.model'].create({
            'partner_id': self.partner_id.id,
            'expected_date': self.expected_date,
            'sequence_no': self.name,
            'order_date': fields.date.today(),
            # 'product': self.move_line_ids_without_package.product_id.id
            'product': self.order_line.product_template_id.id,
            'package': self.order_line.package_field_id.package,
            'detail_width': self.order_line.package_field_id.width,
            'detail_height': self.order_line.package_field_id.height,
            'detail_length': self.order_line.package_field_id.length,
            'detail_weight': self.order_line.package_field_id.maximum_weight,

        })

    def open_package_bundle(self):

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'bundle.model',
            'view_mode': 'kanban,tree,form',
            # 'view_type': 'kanban,tree,form',
            # 'res_id': bundle.id,
            # 'views': [(False, 'kanban')],
            'target': 'current',
            # 'context': "{'create: False'}"

        }


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    package_field_id = fields.Many2one('package.model', string='Package Field', required=True)
# related
