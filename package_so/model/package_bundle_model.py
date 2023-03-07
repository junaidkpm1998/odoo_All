from odoo import models, fields

class PackageBundleModel(models.Model):
    _name = 'bundle.model'
    _rec_name = 'sequence_no'

    partner_id = fields.Many2one("res.partner", string="Partner")
    sequence_no = fields.Text()
    expected_date = fields.Date()
    order_date = fields.Date()
    product = fields.Many2one("product.template")
    quantity = fields.Integer()
    package = fields.Text(string="package")
    detail_width = fields.Text(string="width")
    detail_weight = fields.Text(string="maximum_weight")
    detail_length = fields.Text(string="Length")
    detail_height = fields.Text(string="height")

    def data_view(self):

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'bundle.model',
            'view_mode': 'tree',
            'target': 'current'
        }
