from odoo import models, fields

class Timetable(models.Model):
    _name = 'course.timetable'
    _description = 'Course Timetable'

    name = fields.Char(required=True)
    subject_ids = fields.Many2one('course.subject', required=True)
    course_id = fields.Many2one("course.course", string="Course")
    day_of_week = fields.Selection([
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday')
    ], required=True)
    start_time = fields.Float("Start Time (HH.MM)")
    end_time = fields.Float("End Time (HH.MM)")
