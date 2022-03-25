from odoo import api, fields, models


class Karyawan(models.Model):
    _name = 'perpustakaan.karyawan'
    _description = 'Data Karyawan Perpustakaan'

    kode_karyawan = fields.Integer(string='Kode Karyawan')
    name = fields.Char(string='Nama')
    jenis_kelamin = fields.Selection(string='Jenis Kelamin', selection=[('lakilaki', 'Laki-Laki'), ('perempuan', 'Perempuan'),])
    telp = fields.Char(string='Telepon / HP')
    alamat = fields.Char(string='Alamat')
    
    
    
    
    
    
    
    
    

