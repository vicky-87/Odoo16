from odoo import models, fields, api

class WizardTraininig(models.TransientModel):
    _name = 'wizard.training'
    _description = 'Wizard Training'

    def _default_sesi(self):
        return self.env['training.session'].browse(self._context.get('active_ids'))

    session_id = fields.Many2one(comodel_name='training.session', string='Sesi Training', default=_default_sesi)
    peserta_ids = fields.Many2many(comodel_name='peserta', string='Peserta Training')
    session_ids = fields.Many2many(comodel_name='training.session', string='Multi Training Session', default=_default_sesi)

    def tambah_peserta(self):
        self.session_id.peserta_ids |= self.peserta_ids
        
    def tambah_banyak_peserta(self):
        for session in self.session_ids:
            session.peserta_ids |= self.peserta_ids