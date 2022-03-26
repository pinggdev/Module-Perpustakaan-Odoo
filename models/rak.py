from odoo import api, fields, models


class Rak(models.Model):
    _name = 'perpustakaan.rak'
    _description = 'Rak Buku Perpustakaan'

    kode_rak = fields.Integer(string='Kode Rak')
    name = fields.Char(string='Nama Rak Buku')
    kode_buku_id = fields.Many2one(comodel_name='perpustakaan.buku', string='Kode Buku')
    
    
