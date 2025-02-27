# -*- coding: utf-8 -*-

from odoo import models, fields

class Cliente(models.Model):
    _name = 'hda_videojuegos.cliente' 
    _description = 'Cliente'

    name = fields.Char('Nombre del cliente', required=True, help='Introduce el nombre')
    telefono = fields.Float('Telefono', required=True, help='Introduce el numero de telefono')

    videojuegos_id = fields.Many2one('hda_videojuegos.videojuego', string='Videojuegos')
    pedido_id = fields.One2many('hda_videojuegos.pedido', 'clientes_id' string='Pedido')