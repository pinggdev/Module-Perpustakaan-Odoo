from odoo import api, fields, models


class Anggota(models.Model):
    _name = 'perpustakaan.anggota'
    _description = 'Data Anggota Perpustakaan'

    name = fields.Char(string='Nama')
    jenis_kelamin = fields.Selection(string='Jenis Kelamin', selection=[('lakilaki', 'Laki-Laki'), ('perempuan', 'Perempuan'),])
    fakultas = fields.Char(string='Fakultas')
    jurusan = fields.Char(string='Jurusan')
    angkatan = fields.Char(string='Angkatan')
    alamat = fields.Char(string='Alamat')
    
    
