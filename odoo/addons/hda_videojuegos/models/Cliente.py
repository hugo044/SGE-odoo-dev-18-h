# -*- coding: utf-8 -*-

from odoo import models, fields

class Cliente(models.Model):
    _name = 'hda_videojuegos.cliente' 
    _description = 'Cliente'

    name = fields.Char('Nombre del cliente')
    numero_cliente = fields.Float('Numero de cliente')
    numero_cuenta = fields.Float('Numero de cuenta')
    telefono = fields.Float('Telefono')