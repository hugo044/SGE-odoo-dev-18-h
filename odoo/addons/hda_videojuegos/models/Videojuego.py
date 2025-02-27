# -*- coding: utf-8 -*-

from odoo import models, fields

class Videojuego(models.Model):
    _name = 'hda_videojuegos.videojuego' 
    _description = 'Videojuego'

    name = fields.Char('Titulo',required=True)
    precio = fields.Float('Precio',required=True)
    stock = fields.Float('Stock')
    fecha_lanzamiento= fields.Date('Fecha de lanzamiento')
    portada = fields.Binary('Portada')


    genero_ids = fields.Many2many('hda_videojuegos.genero',relation="hda_videojuegos_genero_videojuego_rel", string='Genero')
    cliente_ids = fields.Many2one('hda_videojuegos.cliente', string='Cliente')
