# -*- coding: utf-8 -*-
from odoo import api, models


class ReportInvoice(models.AbstractModel):
    _name = 'report.account.report_invoice'
    _inherit = 'report.account.report_invoice'
    _description = 'Account report'

    def get_is_printed(self, invoice):
        if invoice.state in ('open', 'paid', 'posted', 'cancel'):
            new_count = (invoice.print_count or 0) + 1
            invoice.sudo().write({
                'isprinted': True,
                'print_count': new_count,
            })
            return new_count
        return 0

    def get_description(self, invoice_line):
        result = []
        res = {}
        description = invoice_line.name or ''
        if invoice_line.product_id:
            code = invoice_line.product_id.default_code or ''
            pname = invoice_line.product_id.name or ''
            extra = (invoice_line.name or '').replace(pname, '').strip()
            description = f"[{code}] {pname} {extra}".strip()
        res['description'] = description
        result.append(res)
        return result

    @api.model
    def _get_report_values(self, docids, data=None):
        res = super()._get_report_values(docids, data=data)
        res.update({
            'get_is_printed': self.get_is_printed,
            'get_description': self.get_description,
        })
        return res


class ReportInvoiceWithPayment(models.AbstractModel):
    _name = 'report.account.report_invoice_with_payments'
    _inherit = 'report.account.report_invoice'
    _description = 'Account report with payment lines'
