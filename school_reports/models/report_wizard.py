# -*- coding: utf-8 -*-
import base64
import io
from odoo import api, fields, models
try:
    import xlsxwriter
except Exception:
    xlsxwriter = None

class SchoolReportCardWizard(models.TransientModel):
    _name = 'school.report.card.wizard'
    _description = 'Print Student Report Cards (PDF)'

    student_ids = fields.Many2many('school.student', string='Students')
    academic_year_id = fields.Many2one('school.academic.year', string='Academic Year')

    def action_print_report_cards(self):
        # call the qweb report action for each selected student (or for all)
        if not self.student_ids:
            students = self.env['school.student'].search([('academic_year_id','=', self.academic_year_id.id)]) if self.academic_year_id else self.env['school.student'].search([])
        else:
            students = self.student_ids
        # report action defined in report_actions.xml (report_student_card)
        return self.env.ref('school_report.report_action_student_card').report_action(students)


class SchoolExportAttendanceWizard(models.TransientModel):
    _name = 'school.report.attendance.xlsx'
    _description = 'Export attendance / grades to XLSX'

    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    class_id = fields.Many2one('school.section', string='Section/Class')
    academic_year_id = fields.Many2one('school.academic.year', string='Academic Year')

    def action_export_xlsx(self):
        # build xlsx in memory and return an ir.actions.act_url to download
        # Use xlsxwriter if available, else fallback to simple CSV (wrapped in xlsx mimetype)
        students = self.env['school.student'].search([
            ('section_id', '=', self.class_id.id),
            ('academic_year_id', '=', self.academic_year_id.id)
        ])

        output = io.BytesIO()
        if xlsxwriter:
            workbook = xlsxwriter.Workbook(output, {'in_memory': True})
            ws = workbook.add_worksheet('Attendance')
            # Header
            headers = ['Student Name', 'Student Code', 'Total Days', 'Present', 'Absent']
            for col, h in enumerate(headers):
                ws.write(0, col, h)
            row = 1
            for st in students:
                # For brevity: example aggregated fields; replace with your attendance model computations
                total = self.env['school.attendance'].search_count([('student_id','=',st.id), ('date','>=', self.start_date), ('date','<=', self.end_date)]) if self.start_date and self.end_date else self.env['school.attendance'].search_count([('student_id','=',st.id)])
                present = self.env['school.attendance'].search_count([('student_id','=',st.id), ('state','=','present'), ('date','>=', self.start_date), ('date','<=', self.end_date)]) if self.start_date and self.end_date else self.env['school.attendance'].search_count([('student_id','=',st.id), ('state','=','present')])
                absent = total - present
                ws.write(row, 0, st.name)
                ws.write(row, 1, st.student_code if hasattr(st, 'student_code') else '')
                ws.write(row, 2, total)
                ws.write(row, 3, present)
                ws.write(row, 4, absent)
                row += 1
            workbook.close()
            output.seek(0)
            data = output.read()
        else:
            # fallback: simple CSV in bytes
            csv_lines = ['Student Name,Student Code,Total Days,Present,Absent\n']
            for st in students:
                total = self.env['school.attendance'].search_count([('student_id','=',st.id)])
                present = self.env['school.attendance'].search_count([('student_id','=',st.id), ('state','=','present')])
                absent = total - present
                csv_lines.append(f'{st.name},{getattr(st, "student_code", "")},{total},{present},{absent}\n')
            data = ''.join(csv_lines).encode('utf-8')

        attachment = self.env['ir.attachment'].create({
            'name': 'attendance_export.xlsx',
            'type': 'binary',
            'datas': base64.b64encode(data),
            'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        })
        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{attachment.id}/datas/attendance_export.xlsx?download=true',
            'target': 'new',
        }
