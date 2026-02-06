from odoo import fields, models

class Teacher(models.Model):
    _name = "school.teacher"
    _description = "Teacher"
    _order = "name"

    name = fields.Char(required=True)
    partner_id = fields.Many2one("res.partner", string="Contact", ondelete="restrict")
    employee_code = fields.Char()
    subject_expertise = fields.Char()
    notes = fields.Text()
    active = fields.Boolean(default=True)
