from odoo import fields, models


class MomentumBrand(models.Model):
    _name = "momentum.brand"
    _description = "Momentum Brand"
    _order = "name"

    name = fields.Char(required=True, index=True)
    code = fields.Char(required=True, index=True)
    active = fields.Boolean(default=True)
    website = fields.Char()
    description = fields.Text()
    color = fields.Integer()

    _sql_constraints = [
        ("momentum_brand_code_unique", "unique(code)", "Brand code must be unique."),
    ]
