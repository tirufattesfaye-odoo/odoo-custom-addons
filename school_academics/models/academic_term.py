from odoo import models, fields

class AcademicTerm(models.Model):
    _name = 'academic.term'
    _description = 'Academic Term'

    name = fields.Char(required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    year_id = fields.Many2one('academic.year', required=True)
    active = fields.Boolean(default=True)
    academic_year_id = fields.Many2one(
        "academic.year",  # make sure this model exists!
        string="Academic Year",
        required=True
    )
