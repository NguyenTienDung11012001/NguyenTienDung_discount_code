# -*- coding: utf-8 -*-
# from odoo import http


# class DiscountCode(http.Controller):
#     @http.route('/discount_code/discount_code', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/discount_code/discount_code/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('discount_code.listing', {
#             'root': '/discount_code/discount_code',
#             'objects': http.request.env['discount_code.discount_code'].search([]),
#         })

#     @http.route('/discount_code/discount_code/objects/<model("discount_code.discount_code"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('discount_code.object', {
#             'object': obj
#         })
