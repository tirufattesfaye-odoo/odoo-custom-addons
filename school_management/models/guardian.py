from odoo import api, fields, models

class Guardian(models.Model):
    _name = "school.guardian"
    _description = "Guardian / Parent"
    _order = "name"

    name = fields.Char(required=True)
    partner_id = fields.Many2one("res.partner", string="Contact", ondelete="restrict")
    relation = fields.Selection([
        ("father","Father"),
        ("mother","Mother"),
        ("relative","Relative"),
        ("other","Other"),
    ], default="other")
    student_ids = fields.Many2many("school.student", "student_guardian_rel",
                                   "guardian_id", "student_id", string="Students")
    notes = fields.Text()
