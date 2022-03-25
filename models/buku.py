from odoo import api, fields, models


class Buku(models.Model):
    _name = 'perpustakaan.buku'
    _description = 'Data Buku Perpustakaan'

    name = fields.Char(string='Judul')
    penulis = fields.Char(string='Penulis')
    penerbit = fields.Char(string='Penerbit')
    tahun_terbit = fields.Date(string='Tahun Terbit')
    
    
    
