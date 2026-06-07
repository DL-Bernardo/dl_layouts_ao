# -*- coding: utf-8 -*-
# Formerly: opc_layouts_aov17
{
    'name': "Angola - DIGITALUB Layouts",
    'summary': """Layouts de Documentos Fiscais Certificados para o Mercado de Angola""",
    'description': """
Modelos e Layouts Visuais Customizados para Documentos Fiscais
=============================================================
Este módulo estende e estiliza a apresentação visual dos relatórios impressos obrigatórios, aplicando a identidade corporativa da DIGITALUB em conformidade com as exigências locais.

Inclui melhorias e designs exclusivos para:
------------------------------------------
* Faturas e Faturas-Recibo (Account Move)
* Guias de Transporte e Guias de Remessa (Stock Picking)
* Orçamentos e Faturas Proforma (Sale Order)
* Recibos de Pagamento (Account Payment)
    """,
    'author': "DIGITALUB ANGOLA, LDA",
    'website': "https://www.digitalub.ao",
    'category': 'Accounting/Localizations',
    'version': '17.0.1.0.1',
    'license': 'OPL-1',           # Licença comercial para a Odoo Store
    'price': 59.00,                # Preço sugerido do add-on de layouts
    'currency': 'EUR',
    
    # Dependências (já refletindo o novo nome do seu módulo core)
    'depends': [
        'base', 
        'account', 
        'sale', 
        'web', 
        'stock', 
        'dl_certification_ao'
    ],
    
    # Arquivos de dados e visualizações
    'data': [
        'security/security.xml',
        'views/account_move_view.xml',
        'views/res_company_view.xml',
        'report/report_account_invoice.xml',
        'report/report_sale_order.xml',
        'report/report_stock_picking.xml',
        'report/report_account_payment.xml',
        'report/report_external_layouts.xml',
    ],
    
    # Vitrine técnica na loja do Odoo
    'images': [
        'static/description/banner.png'
    ],
    
    'installable': True,
    'application': False,          # Definido como False pois atua como extensão/add-on do core
    'auto_install': False,
}
