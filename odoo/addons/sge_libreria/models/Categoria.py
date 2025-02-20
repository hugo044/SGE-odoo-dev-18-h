# -*- coding: utf-8 -*-

from odoo import models, fields

class Categoria(models.Model):
    _name = 'sge_libreria.categoria'
    _description = 'Categoría'

    name = fields.Char('Nombre', required=True)
    description = fields.Char('Descripción')

    libro_ids = fields.One2many('sge_libreria.libro', 'categoria_id', string='Libro')