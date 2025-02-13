# -*- coding: utf-8 -*-

from odoo import models, fields

class Videojuego(models.Model):
    _name = 'hda_videojuegos.videojuego' 
    _description = 'Videojuego'

    name = fields.Char('Titulo',required=True)
    precio = fields.Float('Precio')
    stock = field_name = fields.Float('Stock')
    fecha_lanzamiento = fields.Datetime('Fecha de lanzamiento')
    genero = fields.Char('Genero')