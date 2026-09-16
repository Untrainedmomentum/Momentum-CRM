from odoo import fields, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    momentum_brand_id = fields.Many2one(
        "momentum.brand",
        string="Momentum Brand",
        help="Brand or business unit associated with this lead/opportunity.",
    )
