from odoo import models, fields, api

class SchoolExamMark(models.Model):
    _name = "school.exam.mark"
    _description = "Exam Mark"

    exam_id = fields.Many2one('school.exam', string="Exam", required=True, ondelete='cascade')
    student_id = fields.Many2one('res.partner', string="Student", domain=[('is_student','=',True)], required=True)
    section_id = fields.Many2one(related="exam_id.section_id", store=True)
    academic_year_id = fields.Many2one(related="exam_id.academic_year_id", store=True)
    line_ids = fields.One2many('school.exam.mark.line', 'mark_id', string="Marks")

    total_marks = fields.Float(compute="_compute_total", store=True)
    percentage = fields.Float(compute="_compute_total", store=True)
    result = fields.Selection([('pass','Pass'),('fail','Fail')], compute="_compute_total", store=True)

    @api.depends('line_ids.obtained_marks', 'line_ids.max_marks')
    def _compute_total(self):
        for rec in self:
            total = sum(line.obtained_marks for line in rec.line_ids)
            max_total = sum(line.max_marks for line in rec.line_ids)
            rec.total_marks = total
            rec.percentage = (total / max_total * 100) if max_total > 0 else 0
            rec.result = 'pass' if all(line.obtained_marks >= line.pass_marks for line in rec.line_ids) else 'fail'


class SchoolExamMarkLine(models.Model):
    _name = "school.exam.mark.line"
    _description = "Exam Mark Line"

    mark_id = fields.Many2one('school.exam.mark', string="Exam Mark", ondelete='cascade')
    subject_id = fields.Many2one('school.subject', string="Subject", required=True)
    max_marks = fields.Float(default=100.0)
    pass_marks = fields.Float(default=40.0)
    obtained_marks = fields.Float()
