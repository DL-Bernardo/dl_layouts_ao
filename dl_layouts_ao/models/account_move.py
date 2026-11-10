# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class AccountMove(models.Model):
    _inherit = "account.move"

    @api.depends('partner_id', 'partner_shipping_id')
    def _get_view_transportation_data(self):
        for rec in self:
            if rec.partner_id and rec.partner_shipping_id and rec.partner_shipping_id != rec.partner_id:
                rec.view_transportation_data = True
            else:
                rec.view_transportation_data = False

    loading_date = fields.Datetime('Date of Loading', readonly=False)
    unloading_date = fields.Datetime('Date of Unloading', readonly=False)
    vehicle_registration = fields.Char('Vehicle Registration', readonly=False)
    isprinted = fields.Boolean('Impresso', copy=False)
    print_count = fields.Integer('Contador de Impressões', default=0, copy=False)
    view_transportation_data = fields.Boolean(
        'View Transportation Data',
        compute='_get_view_transportation_data',
    )

    def _get_report_base_filename(self):
        self.ensure_one()
        doc_num = getattr(self, 'internal_number', False) or self.name or ''
        return (
            self.move_type == 'out_invoice' and self.state == 'draft' and _('Draft Invoice')
            or self.move_type == 'out_invoice' and self.state in ('open', 'in_payment', 'paid', 'posted') and _('Invoice - %s') % doc_num
            or self.move_type == 'out_invoice' and self.state == 'cancel' and _('Cancelled Invoice - %s') % doc_num
            or self.move_type == 'out_refund' and self.state == 'draft' and _('Credit Note')
            or self.move_type == 'out_refund' and _('Credit Note - %s') % doc_num
            or self.move_type == 'out_refund' and self.state == 'cancel' and _('Cancelled Credit Note - %s') % doc_num
            or self.move_type == 'in_invoice' and self.state == 'draft' and _('Vendor Bill')
            or self.move_type == 'in_invoice' and self.state in ('open', 'in_payment', 'paid', 'posted') and _('Vendor Bill - %s') % doc_num
            or self.move_type == 'in_invoice' and self.state == 'cancel' and _('Cancelled Vendor Bill - %s') % doc_num
            or self.move_type == 'in_refund' and self.state == 'draft' and _('Vendor Credit Note')
            or self.move_type == 'in_refund' and _('Vendor Credit Note - %s') % doc_num
            or self.move_type == 'in_refund' and self.state == 'cancel' and _('Cancelled Vendor Credit Note - %s') % doc_num
            or super()._get_report_base_filename()
        )
