from odoo import models, fields
class EmployeeLevel(models.Model):
    _name = "employee.level"
    _description = "employee Model"
    _rec_name = "level"

    level = fields.Char()
    salary = fields.Integer()
