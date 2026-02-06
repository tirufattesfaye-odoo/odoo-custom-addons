from odoo import models, fields, api

class SchoolExam(models.Model):
    _name = "school.exam"
    _description = "Exam"

    name = fields.Char(required=True)
    academic_year_id = fields.Many2one('school.academic.year', string="Academic Year", required=True)
    term_id = fields.Many2one('school.academic.term', string="Term")
    section_id = fields.Many2one('school.section', string="Class/Section", required=True)
    date_start = fields.Date()
    date_end = fields.Date()
    exam_line_ids = fields.One2many('school.exam.line', 'exam_id', string="Exam Lines")


class SchoolExamLine(models.Model):
    _name = "school.exam.line"
    _description = "Exam Subject Line"

    exam_id = fields.Many2one('school.exam', string="Exam", ondelete='cascade')
    subject_id = fields.Many2one('school.subject', string="Subject", required=True)
    max_marks = fields.Float(default=100.0)
    pass_marks = fields.Float(default=40.0)
