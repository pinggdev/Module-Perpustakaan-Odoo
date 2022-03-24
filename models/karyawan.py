from odoo import api, fields, models


class Karyawan(models.Model):
    _name = 'perpustakaan.karyawan'
    _description = 'Data Karyawan Perpustakaan'

    kode_karyawan = fields.Char(string='Kode Karyawan')
    name = fields.Char(string='Nama')
    jenis_kelamin = fields.Selection(string='Jenis Kelamin', selection=[('lakilaki', 'Laki-Laki'), ('perempuan', 'Perempuan'),])
    jabatan = fields.Selection(string='Jabatan', selection=[('manager', 'Manager'), ('kepala_perpus', 'Kepala Perpustakaan'), ('petugas_buku', 'Petugas Buku'), ('penjaga_kebersihan', 'Penjaga Kebersihan')])
    nomor_telepon = fields.Char(string='Nomor Telepon / HP')
    alamat = fields.Char(string='Alamat')
    
    
    
    
    

