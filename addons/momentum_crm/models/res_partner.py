from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    momentum_brand_id = fields.Many2one(
        "momentum.brand",
        string="Momentum Brand",
        help="Internal brand or business unit this contact belongs to.",
    )
