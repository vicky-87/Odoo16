from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'

    product_training = fields.Selection(string='Jenis Produk Training', selection=[('non_training', 'Non Produk Training Training'), ('konsumsi', 'Konsumsi Training'), ('training_Kit', 'Peralatan Training')], default='non_training')