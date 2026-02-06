from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class AcademicYear(models.Model):
    _name = "school.academic.year"
    _description = "Academic Year"
    _order = "date_start desc"

    name = fields.Char(string="Year Name", required=True)
    code = fields.Char(string="Code", required=True)
    date_start = fields.Date(string="Start Date", required=True)
    date_end = fields.Date(string="End Date", required=True)
    active = fields.Boolean(string="Active", default=True)
    state = fields.Selection(
        [
            ("planning", "Planning"),
            ("running", "Running"),
            ("closed", "Closed"),
        ],
        string="Status",
        default="planning",
        tracking=True,
    )

    _sql_constraints = [
        ("code_unique", "unique(code)", "Academic year code must be unique."),
    ]

    @api.constrains('date_start', 'date_end')
    def _check_dates(self):
        for record in self:
            # Only compare if both dates are set
            if record.date_start and record.date_end:
                if record.date_end < record.date_start:
                    raise ValidationError(_("End date cannot be before start date."))

    @api.constrains("date_start", "date_end", "active")
    def _check_overlap(self):
        for record in self:
            overlap = self.search(
                [
                    ("id", "!=", record.id),
                    ("active", "=", True),
                    ("date_start", "<=", record.date_end),
                    ("date_end", ">=", record.date_start),
                ],
                limit=1,
            )
            if overlap:
                raise ValidationError(_("Academic years cannot overlap."))
