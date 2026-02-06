from odoo import models, fields, api


class BookDetails(models.Model):
    _name = 'book.details'
    _description = 'book'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    title = fields.Char(string='Book_Title', required=True)
    author = fields.Char(string='Author')
    publisher = fields.Char(string='Publisher')
    published_date = fields.Date(string='Published Date')
    book_age = fields.Integer(string='Book Age')
    cover = fields.Image(string='Book Cover')