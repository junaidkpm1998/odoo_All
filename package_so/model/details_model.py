from odoo import models, fields

class Dview(models.Model):
    _name = 'details.model'

    sale11 = fields.Many2one("sale.order.line")
    product = fields.Many2one('product.template', string='product')
    package = fields.Text(string="package")
