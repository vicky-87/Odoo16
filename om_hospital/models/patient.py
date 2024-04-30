from odoo import api, fields, models

# class model untuk pasien rumah sakit
class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Patient Name', tracking=True)
    ref = fields.Char(string='Reference')
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection(string='Gender', selection=[('male', 'Male'), ('female', 'Female')], tracking=True)
    active = fields.Boolean(string='Active', default=True)
   