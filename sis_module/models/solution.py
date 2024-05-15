# -*- coding: utf-8 -*-

from odoo import models, fields


class Solution(models.Model):
    _name = "sis_module.solutions"
    _description = "Solutions"
    _rec_name = "name"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description", required=True)
    proposal = fields.Char(string="Proposal", required=True)

    usedBy = fields.Many2one(
        comodel_name="sis_module.clients", string="Used By", required=True)
    builtWith = fields.Many2many(
        comodel_name="sis_module.technologies", string="Built With", required=True)

    # Untuk mendapatkan UUID creator, dapat mengakses field create_uid
