{
    "name": "Momentum CRM",
    "version": "19.0.1.0.0",
    "summary": "Untrained Momentum CRM/operations layer on Odoo Community",
    "category": "Sales/CRM",
    "author": "Untrained Momentum",
    "website": "https://untrainedmomentum.com",
    "license": "LGPL-3",
    "depends": ["base", "contacts", "crm", "project"],
    "data": [
        "security/ir.model.access.csv",
        "views/momentum_brand_views.xml",
        "views/res_partner_views.xml",
        "views/crm_lead_views.xml",
        "views/project_views.xml",
        "data/momentum_brand_demo.xml"
    ],
    "installable": True,
    "application": True,
}
