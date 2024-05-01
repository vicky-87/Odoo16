from odoo import api, fields, models

# class model untuk pasien rumah sakit
class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    appointment_time = fields.Datetime(string='Appointment Time')
    booking_date = fields.Date(string='Booking Date')
