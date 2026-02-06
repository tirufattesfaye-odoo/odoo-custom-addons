from odoo import models, fields, api, _

class SchoolAttendance(models.Model):
    _name = "school.attendance"
    _description = "School Attendance"

    name = fields.Char(string="Name", compute="_compute_name", store=True)
    date = fields.Date(string="Date", required=True, default=fields.Date.today)
    class_id = fields.Many2one("school.class", string="Class", required=True)
    teacher_id = fields.Many2one("school.teacher", string="Teacher")
    line_ids = fields.One2many("school.attendance.line", "attendance_id", string="Attendance Lines")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
    ], string="Status", default="draft")

    @api.depends("class_id", "date")
    def _compute_name(self):
        for record in self:
            record.name = f"{record.class_id.name} - {record.date}" if record.class_id and record.date else "Attendance"

    def action_confirm(self):
        self.write({"state": "confirmed"})

    def action_draft(self):
        self.write({"state": "draft"})


class SchoolAttendanceLine(models.Model):
    _name = "school.attendance.line"
    _description = "School Attendance Line"

    attendance_id = fields.Many2one("school.attendance", string="Attendance Sheet", ondelete="cascade")
    student_id = fields.Many2one("school.student", string="Student", required=True)
    status = fields.Selection([
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
        ('excused', 'Excused'),
    ], string="Status", default="present")
    remark = fields.Char(string="Remark")
