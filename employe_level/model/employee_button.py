from odoo import models, fields, api


class EmployeePageButton(models.Model):
    _inherit = 'hr.employee'

    employee_level = fields.Many2one('employee.level', string="level")
    employee_pm = fields.Boolean(default=False)


    def employee_promote(self):
        print(self.employee_level)
        self.employee_level = self.employee_level.id + 1
        # if self.employee_level.id == 4:
        if self.employee_level.id == self.env['employee.level'].search([])[-1].id:
            self.employee_pm = True
            print("mmmm")

    @api.onchange('employee_level')
    def employee_onchange(self):
        if self.employee_level.id == self.env['employee.level'].search([])[-1].id:
            self.employee_pm = True
        else:
            self.employee_pm = False
