# -*- coding: utf-8 -*-

from odoo import models, fields

class Libro(models.Model):
    _name = 'sge_libreria.libro'
    _description = 'Libro'

    name = fields.Char('Nombre', required=True)
    description = fields.Char('Descripción')

    name = fields.Char('Titulo',required=True)
    precio = fields.Monetary('Precio')
    currency_id = fields.Many2one('res.currency', string='Moneda')
    ejemplares = fields.Integer('Ejemplares')
    fecha_compra = fields.Date('Fecha de mano')
    segmano = fields.Boolean('Segunda mano')
    estado = fields.Selection([
        ('0', 'Bueno'),
        ('1', 'Regular'),
        ('2', 'Malo'),
    ], string='Estado',default ='0')

    categoria_id = fields.Many2one('sge_libreria.categoria', string='Categoria')