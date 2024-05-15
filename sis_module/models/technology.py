# -*- coding: utf-8 -*-

from odoo import models, fields


class Technology(models.Model):
    _name = "sis_module.technologies"
    _description = "Technologies"
    _rec_name = "name"

    name = fields.Char(string="Name", required=True)
    utility = fields.Text(string="Utility", required=True)
    logo = fields.Image(string="Logo", required=True)
    resource = fields.Char(string="Resource", required=True)

    build = fields.Many2many(
        comodel_name="sis_module.solutions", string="Build")
    hasRisk = fields.Many2many(
        comodel_name="sis_module.vulnerabilities", string="Has Risk")
