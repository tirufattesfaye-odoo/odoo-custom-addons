from odoo import models, fields, api

class SchoolFee(models.Model):
    _name = 'school.fee'
    _description = 'School Fee'

    name = fields.Char(string="Fee Reference", required=True, copy=False, readonly=True,
                       default=lambda self: self.env['ir.sequence'].next_by_code('school.fee'))
    student_id = fields.Many2one('school.student', string="Student", required=True)
    amount = fields.Monetary(string="Fee Amount", required=True)
    currency_id = fields.Many2one('res.currency', string="Currency",
                                  default=lambda self: self.env.company.currency_id)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('invoiced', 'Invoiced'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled')
    ], string="Status", default='draft')

    invoice_id = fields.Many2one('account.move', string="Invoice", readonly=True)

    def action_create_invoice(self):
        for fee in self:
            if fee.invoice_id:
                continue
            invoice_vals = {
                'move_type': 'out_invoice',
                'partner_id': fee.student_id.guardian_id.partner_id.id,  # Assuming guardian is linked to res.partner
                'invoice_line_ids': [(0, 0, {
                    'name': f"School Fee for {fee.student_id.name}",
                    'quantity': 1,
                    'price_unit': fee.amount,
                })],
            }
            invoice = self.env['account.move'].create(invoice_vals)
            fee.invoice_id = invoice.id
            fee.state = 'invoiced'

    def action_mark_paid(self):
        for fee in self:
            if fee.invoice_id and fee.invoice_id.payment_state == 'paid':
                fee.state = 'paid'
