from odoo import models, fields, api


class Peserta(models.Model):
    _name = 'peserta'
    _description = 'Peserta'
    _inherits       = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one(comodel_name='res.partner', string='Partner ID', ondelete="cascade", required=True)
    pendidikan = fields.Selection(string='Pendidikan', selection=[('smp', 'SMP'), ('sma', 'SMA'), ('diploma', 'D1/D2/D3'), ('s1', 'S1'), ('s2', 'S2'),])
    pekerjaan  = fields.Char(string='Pekerjaan')
    is_menikah = fields.Boolean(string='Menikah?', default=False)
    nama_pasangan = fields.Char(string='Nama Istri/Suami')
    hp_pasangan = fields.Char(string='No HP Istri/Suami')
    tmp_lahir = fields.Char(string='Tempat Lahir')
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    no_peserta = fields.Char(string='NO Peserta', readonly=True)
    

    @api.model
    def create(self, values):
        # Add code here
        values['no_peserta'] = self.env['ir.sequnce'].next_by_code('seq.peserta')
        return super(Peserta, self).create(values)
    

    
    
    