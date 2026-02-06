from odoo import models, fields, api


class RentPayment(models.Model):
    _name = 'rent.payment'
    _description = 'Rent Payment'

    name = fields.Char(string='Payment Reference', required=True, copy=False, readonly=True, default='New')


    lease_id = fields.Many2one('lease.management', string='Lease', required=True)
    payment_date = fields.Date(string='Payment Date', required=True, default=fields.Date.today)
    amount_paid = fields.Float(string='Amount Paid', required=True)
    status = fields.Selection([
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid')
    ], string='Status', default='unpaid')
    note = fields.Text(string='Note')


    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('rent.payment') or 'New'
        return super(RentPayment, self).create(vals)

    def action_payment(self):
        self.status = 'paid'

    @api.onchange('lease_id')
    def _onchange_lease_id(self):
        if self.lease_id:
            self.amount_paid = self.lease_id.monthly_rent
        else:
            self.amount_paid = 0.0