from odoo import models, fields, api

class JabatanWizard(models.Model):
    _name = 'jabatan.wizard'
    _description = 'Jabatan Wizard'

    jabatan_id = fields.Many2one(comodel_name='jabatan', string='Jabatan')
    pejabat_id = fields.Many2one(comodel_name='instruktur', string='Pejabat')

    def update_jabatan(self):
        self.pejabat_id.write({'jabatan_id': self.jabatan_id.id})
        self.jabatan_id.write({'pejabat_id': self.pejabat_id.id})

        return {'type': 'ir.actions.act_window_close'}