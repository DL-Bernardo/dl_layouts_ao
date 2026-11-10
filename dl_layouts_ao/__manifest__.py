# -*- coding: utf-8 -*-
{
    'name': 'Angola Invoice & Document Layouts (AGT Compliant)',
    'summary': 'Certified Fiscal Document Layouts & Reports for Angola Market (AGT Compliant)',
    'description': """
Modelos e Layouts Visuais Customizados para Documentos Fiscais (Angola AGT)
===========================================================================
Este módulo estende e estiliza a apresentação visual dos relatórios impressos obrigatórios, aplicando o padrão executivo em conformidade com as exigências fiscais da AGT em Angola.

Inclui melhorias e designs exclusivos para:
------------------------------------------
* Faturas, Faturas-Recibo, Notas de Crédito e Débito (Account Move)
* Guias de Transporte e Guias de Remessa com Múltiplas Vias (Stock Picking)
* Orçamentos e Faturas Proforma (Sale Order)
* Recibos de Pagamento com Discriminação de Faturas e Retenção (Account Payment)
* Suporte a Múltiplos IBANs nas Contas Bancárias da Empresa
* 100% compatível com Odoo 15, 16, 17, 18, 19 e 20
    """,
    'author': "DIGITALUB ANGOLA, LDA",
    'website': "https://www.digitalub.ao",
    'support': "suporte@digitalub.ao",
    'category': 'Accounting/Localizations',
    'version': '17.0.1.0.9',
    'license': 'OPL-1',
    'price': 79.0,
    'currency': 'USD',
    'depends': [
        'base',
        'account',
        'sale',
        'web',
        'stock',
    ],
    'data': [
        'security/security.xml',
        'views/account_move_view.xml',
        'views/res_company_view.xml',
        'views/res_partner_bank_views.xml',
        'report/report_account_invoice.xml',
        'report/report_sale_order.xml',
        'report/report_stock_picking.xml',
        'report/report_account_payment.xml',
        'report/report_external_layouts.xml',
    ],
    'images': [
        'static/description/banner.png',
        'static/description/step1_layout_select.png',
        'static/description/step2_layout_customize.png',
        'static/description/step3_layout_invoice.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
