from odoo import models, fields

class Subject(models.Model):
    _name = 'course.subject'
    _description = 'Course Subject'

    name = fields.Char(required=True)
    code = fields.Char()
    course_id = fields.Many2one('course.course', string="Course")
    teacher_id = fields.Many2one("school.teacher", string="Teacher")
    credit_hours = fields.Integer(default=3)
    active = fields.Boolean(default=True)
