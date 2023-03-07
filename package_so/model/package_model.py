from odoo import models, fields
class PackageModel(models.Model):
    _name = "package.model"
    _description = "packages Model"
    _rec_name = "package"

    package = fields.Char()
    width = fields.Float()
    height = fields.Float()
    length = fields.Float()
    maximum_weight = fields.Float()
    package_model_id = fields.Many2one("sale.order")
