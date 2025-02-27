# -*- coding: utf-8 -*-

from odoo import models, fields

class Cliente(models.Model):
    _name = 'hda_videojuegos.cliente' 
    _description = 'Cliente'

    name = fields.Char('Nombre del cliente', required=True, help='Introduce el nombre')
    telefono = fields.Integer('Telefono', required=True, help='Introduce el numero de telefono')

    videojuegos_id = fields.One2many('hda_videojuegos.videojuego', 'cliente_ids',string='Videojuegos')
    pedido_id = fields.One2many('hda_videojuegos.pedido', 'clientes_ids',string='Pedido')