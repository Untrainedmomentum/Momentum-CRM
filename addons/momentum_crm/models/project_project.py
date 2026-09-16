from odoo import fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"

    momentum_brand_id = fields.Many2one(
        "momentum.brand",
        string="Momentum Brand",
        help="Brand or business unit this project supports.",
    )
