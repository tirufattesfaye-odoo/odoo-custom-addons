from odoo import models, fields

class Course(models.Model):
    _name = 'course.course'
    _description = 'Course'

    name = fields.Char(required=True)
    code = fields.Char()
    subject_ids = fields.One2many('course.subject', 'course_id', string="Subjects")
    active = fields.Boolean(default=True)
