# -*- coding: utf-8 -*-
# from odoo import http


# class Perpustakaanmodule(http.Controller):
#     @http.route('/perpustakaanmodule/perpustakaanmodule/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/perpustakaanmodule/perpustakaanmodule/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('perpustakaanmodule.listing', {
#             'root': '/perpustakaanmodule/perpustakaanmodule',
#             'objects': http.request.env['perpustakaanmodule.perpustakaanmodule'].search([]),
#         })

#     @http.route('/perpustakaanmodule/perpustakaanmodule/objects/<model("perpustakaanmodule.perpustakaanmodule"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('perpustakaanmodule.object', {
#             'object': obj
#         })
