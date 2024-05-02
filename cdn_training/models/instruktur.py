from odoo import models, fields, api

class Instruktur(models.Model):
    _name           = 'instruktur'
    _description    = 'Instruktur'
    _inherits       = {'res.partner': 'partner_id'}

    partner_id      = fields.Many2one(comodel_name='res.partner', string='Partner', required=True, ondelete='cascade')
    keahlian_ids    = fields.Many2many(comodel_name='keahlian', string='Keahlian')
    jabatan_id = fields.Many2one(comodel_name='jabatan', string='Jabatan')
    jabatan_staff = fields.Char(string='Jabatan Staff')
    jenis_jabatan = fields.Selection(string='Jenis Jabatan', related='jabatan_id.jenis_jabatan')
    
    def action_update_jabatan(self):
        self.jabatan_id.pejabat = self.id
        return True

class Keahlian(models.Model):
    _name           = 'keahlian'
    _description    = 'Keahlian'

    name            = fields.Char(string='Keahlian', required=True)
