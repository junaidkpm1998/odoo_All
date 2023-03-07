from odoo import fields, models, api

class SaleOrdera(models.Model):
    _inherit = 'stock.picking'

    def button_validate(self):
        value = super(SaleOrdera, self).button_validate()
        self.sale_id.delivery_done = True
        # print(self.sale_id)
        return value
