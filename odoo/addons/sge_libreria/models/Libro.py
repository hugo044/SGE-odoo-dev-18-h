# -*- coding: utf-8 -*-

from odoo import models, fields

class Libro(models.Model):
    _name = 'sge_libreria.libro'
    _description = 'Libro'

    name = fields.Char('Nombre', required=True)
    description = fields.Char('Descripción')

    name = fields.Char('Titulo',required=True)
    precio = fields.Float('Precio')
    ejemplares = fields.Integer('Ejemplares')
    fecha_compra = fields.Date('Fecha de mano')
    segmano = fields.Boolean('Segunda mano')
    estado = fields.Selection([
        ('0', 'Bueno'),
        ('1', 'Regular'),
        ('2', 'Malo'),
    ], string='Estado',default ='0')