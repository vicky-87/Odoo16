# -*- coding: utf-8 -*-

from odoo import models, fields


class Client(models.Model):
    _name = "sis_module.clients"
    _description = "Clients"
    _rec_name = "name"

    name = fields.Char(string="Name", required=True)
    outline = fields.Text(string="Outline", required=True)
    industry = fields.Selection(
        selection=[("small/medium", "Small or Medium"), ("corporate", "Corporate"), ("enterprise", "Enterprise")], string="Industry", required=True)
    logo = fields.Image(string="Logo", required=True)
    phoneNumber = fields.Char(string="Phone Number", required=True)

    uses = fields.One2many(comodel_name="sis_module.solutions",
                           inverse_name="usedBy", string="Uses", required=True)

    # Untuk mendapatkan UUID handler, dapat mengakses field create_uid
