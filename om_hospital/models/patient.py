from odoo import api, fields, models
from datetime import date

# class model untuk pasien rumah sakit
class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    # _rec_name = 'name'

    name = fields.Char(string='Patient Name', tracking=True)
    date_of_birth = fields.Date(string='Date Of Birth')
    ref = fields.Char(string='Reference')
    age = fields.Integer(string='Age', compute='_compute_age' ,tracking=True)
    gender = fields.Selection(string='Gender', selection=[('male', 'Male'), ('female', 'Female')], tracking=True)
    active = fields.Boolean(string='Active', default=True)
    appointment_id = fields.Many2one('hospital.appointment', string='Appointments')
   
    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            # print("date.today()", "date.today()")
            if rec.date_of_birth:
                # print("rec", rec, rec.name, rec.date_of_birth.year)
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1