from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    purchase_training = fields.Selection(string='Jenis Purchase Training', selection=[('non_training', 'Non Produk Training Training'), 
                                                                                    ('konsumsi', 'Konsumsi Training'), 
                                                                                    ('training_Kit', 'Peralatan Training')], default='non_training')