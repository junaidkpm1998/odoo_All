from odoo import models, fields

# Create a new model for the custom field
class SaleOrderLinePackageField(models.Model):
    _name = 'sale.order.line.package.field'
    package_field = fields.Char(string='Custom Field')
