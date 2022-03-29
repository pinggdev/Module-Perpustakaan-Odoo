from odoo import api, fields, models


class Peminjaman(models.Model):
    _name = 'perpustakaan.peminjaman'
    _description = 'Peminjaman Perpustakaan'

    peminjamanbukudetail_ids = fields.One2many(
        comodel_name='perpustakaan.peminjamanbukudetail', 
        inverse_name='peminjaman_id', 
        string='Peminajaman Buku Detail')
    
    name = fields.Char(string='Kode Pinjam')
    tgl_pinjam = fields.Datetime('Tanggal Pinjam', default=fields.Datetime.now())
    tgl_pengembalian = fields.Date(string='', default=fields.Date.today())
    kode_karyawan_id = fields.Many2one(comodel_name='perpustakaan.karyawan', string='Karyawan')
    kode_anggota_id = fields.Many2one(comodel_name='perpustakaan.anggota', string='Anggota')
    total = fields.Integer(compute='_compute_total', string='Total', store=True)
    
    @api.depends('peminjamanbukudetail_ids')
    def _compute_total(self):
        for record in self:
            a = sum(self.env['perpustakaan.peminjamanbukudetail'].search([('peminjaman_id', '=', record.id)]).mapped('qty'))
            record.total = a
    # kode_buku_id = fields.Many2one(comodel_name='perpustakaan.buku', string='Buku')
    
    

class PeminjamanBukuDetail(models.Model):
    _name = 'perpustakaan.peminjamanbukudetail'
    _description = 'New Description'

    peminjaman_id = fields.Many2one(comodel_name='perpustakaan.peminjaman', string='Peminjaman Buku Perpustkaan')
    buku_id = fields.Many2one(comodel_name='perpustakaan.buku', string='Buku')
    
    name = fields.Char(string='Name')
    qty = fields.Integer(string='Jumlah Buku Yang Di Pinjam')
    
    @api.model
    def create(self, vals):
        record = super(PeminjamanBukuDetail, self).create(vals)
        if record.qty:
            self.env['perpustakaan.buku'].search([('id', '=', record.buku_id.id)]).write({'stok':record.buku_id.stok-record.qty})
            return record

