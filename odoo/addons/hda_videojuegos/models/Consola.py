from odoo import models, fields

class Consola(models.Model):
    _name = 'hda_videojuegos.consola'
    _description = 'Consola'

    name = fields.Char('Nombre', required=True)
    precio = fields.Float('Precio')
    modelo = fields.Char('Modelo')