from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Jabatan(models.Model):
    _name = 'jabatan'
    _description = 'Jabatan'
    # _inherits       = {'res.partner': 'instruktur'}

    name = fields.Char(string='Nama Jabatan', required=True)
    jenis_jabatan = fields.Selection(string='Jenis Jabatan', selection=[('1', 'Kepala Lembaga'), ('2', 'Wakil Lembaga'), ('3', 'Staff')])
    keterangan = fields.Text('keterangan')
    pejabat = fields.Many2one(comodel_name='instruktur', string='Pejabat', readonly=True)

    @api.constrains('jenis_jabatan')
    def _check_jabatan_constraints(self):
        for record in self:
            if record.jenis_jabatan == 'kepala':
                existing_kepala = self.search([('jenis_jabatan', '=', 'kepala')])
                if len(existing_kepala) > 1 or (len(existing_kepala) == 1 and existing_kepala.id != record.id):
                    raise ValidationError("Hanya boleh ada satu Kepala/Pimpinan Lembaga!")
            elif record.jenis_jabatan == 'wakil_kepala':
                existing_wakil = self.search([('jenis_jabatan', '=', 'wakil_kepala')])
                if len(existing_wakil) > 1 or (len(existing_wakil) == 1 and existing_wakil.id != record.id):
                    raise ValidationError("Hanya boleh ada satu Wakil Kepala Lembaga Saja!")
    
    