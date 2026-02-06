# -*- coding: utf-8 -*-
from odoo import api, fields, models

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    staff_code = fields.Char(
        string='Staff Code',
        readonly=True,
        copy=False,
        default=lambda self: self.env['ir.sequence'].next_by_code('school.staff') if self.env.ref('school_hr.seq_school_staff', raise_if_not_found=False) is None else self.env['ir.sequence'].next_by_code('school.staff')
    )
    staff_role = fields.Selection([
        ('teacher', 'Teacher'),
        ('admin', 'Administrator'),
        ('accountant', 'Accountant'),
        ('other', 'Other'),
    ], string='Staff Role', default='teacher', required=True)
    # link teachers to academic concepts defined in school_academics
    course_ids = fields.Many2many('course.course', string='Courses')
    section_ids = fields.Many2many('course.subject', string='Sections')

    @api.model_create_multi
    def create(self, vals_list):
        # ensure staff_code using our sequence if not provided
        for vals in vals_list:
            if not vals.get('staff_code'):
                vals['staff_code'] = self.env['ir.sequence'].next_by_code('school.staff') or '/'
        return super(HrEmployee, self).create(vals_list)


class SchoolTeacherAssignment(models.Model):
    _name = 'school.teacher.assignment'
    _description = 'Assign Teacher to Course / Section'

    teacher_id = fields.Many2one('hr.employee', string='Teacher', domain=[('staff_role', '=', 'teacher')], required=True)
    course_id = fields.Many2one('school.course', string='Course', required=True)
    section_id = fields.Many2one('school.section', string='Section')
    academic_year_id = fields.Many2one('school.academic.year', string='Academic Year')
    note = fields.Text('Notes')
    active = fields.Boolean(default=True)
