from odoo import api, fields, models

# class model untuk pasien rumah sakit
class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'patient_id'

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    gender = fields.Selection(related='patient_id.gender')
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)
    ref = fields.Char(string='Reference')
    prescription = fields.Html(string='Prescription')
    
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string='Priority')
    # help='Gives the sequence order when displaying a list of MRP documents.')

    @api.onchange('patient.id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref