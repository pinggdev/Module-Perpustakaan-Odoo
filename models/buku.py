from odoo import api, fields, models


class Buku(models.Model):
    _name = 'perpustakaan.buku'
    _description = 'Data Buku Perpustakaan'

    kode_buku = fields.Integer(string='Kode Buku')
    name = fields.Char(string='Judul')
    penulis = fields.Char(string='Penulis')
    penerbit = fields.Char(string='Penerbit')
    tahun_terbit = fields.Date(string='Tahun Terbit')
    stok = fields.Integer(string='Stok Buku')
    
    
    
    
