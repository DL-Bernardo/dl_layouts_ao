# Angola - DIGITALUB Layouts (dl_layouts_ao)

> Módulo de extensão visual para **layouts de documentos fiscais e comerciais** no Odoo 17, totalmente adaptado às exigências e padrões do mercado de Angola ??.

---

## ? Visão Geral

Este módulo foi desenvolvido pela **DIGITALUB** para estender e padronizar a identidade visual dos documentos impressos gerados pelo Odoo. Ele garante uma apresentação profissional, limpa e alinhada com os requisitos de conformidade exigidos localmente.

### ? Documentos Customizados Incluídos:
* **Faturas & Faturas-Recibo:** Disposição clara dos dados fiscais, tabelas de impostos, retenções na fonte e o bloco de assinaturas/hashes.
* **Guias de Transporte / Remessa (Stock Picking):** Otimizado para logística e fiscalização em trânsito (dados do motorista, viatura, horas de carga, etc.).
* **Orçamentos & Faturas Proforma (Sale Order):** Propostas comerciais elegantes para aumentar o impacto visual junto aos clientes.
* **Recibos de Pagamento (Account Payment):** Modelos de quitação financeira estruturados.
* **Layout Externo Customizado:** Cabeçalhos inteligentes com logotipos redimensionados dinamicamente e rodapés institucionais em todas as páginas.

---

## ?? Dependências Obrigatórias

Por ser uma extensão com foco em documentos certificados, este módulo possui dependências estritas e requer o core de certificação da DIGITALUB instalado:

* `dl_certification_ao` (Módulo Core de Certificação Fiscal - Angola)
* Módulos nativos do Odoo: `base`, `account`, `sale`, `web`, `stock`

---

## ? Estrutura do Módulo

O repositório segue as melhores práticas de desenvolvimento da Odoo e está organizado da seguinte forma:

```text
dl_layouts_ao/
??? data/                  # Dados estáticos e configurações iniciais
??? models/                # Extensões de modelos Python (regras de negócio)
??? report/                # Arquivos QWeb (XML) com as estruturas dos relatórios
??? security/              # Regras de segurança e permissões de acesso (ir.model.access.csv)
??? static/                
?   ??? description/       # Ícone, banners e documentação para a Odoo Store
?   ??? src/               # Estilos CSS/SCSS (se aplicável)
??? views/                 # Interfaces XML e heranças de views existentes