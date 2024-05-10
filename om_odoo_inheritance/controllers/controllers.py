# -*- coding: utf-8 -*-
# from odoo import http


# class OmOdooInheritance(http.Controller):
#     @http.route('/om_odoo_inheritance/om_odoo_inheritance', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_odoo_inheritance/om_odoo_inheritance/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_odoo_inheritance.listing', {
#             'root': '/om_odoo_inheritance/om_odoo_inheritance',
#             'objects': http.request.env['om_odoo_inheritance.om_odoo_inheritance'].search([]),
#         })

#     @http.route('/om_odoo_inheritance/om_odoo_inheritance/objects/<model("om_odoo_inheritance.om_odoo_inheritance"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_odoo_inheritance.object', {
#             'object': obj
#         })
