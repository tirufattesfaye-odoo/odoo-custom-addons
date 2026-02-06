from odoo import models, fields

class AcademicYear(models.Model):
    _name = 'academic.year'
    _description = 'Academic Year'

    name = fields.Char(required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    term_ids = fields.One2many('academic.term', 'year_id', string="Terms")
    active = fields.Boolean(default=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('running', 'Running'),
        ('done', 'Done'),
    ], string="Status", default='draft')
