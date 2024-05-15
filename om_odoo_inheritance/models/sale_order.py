from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def test_function(self):
        return
