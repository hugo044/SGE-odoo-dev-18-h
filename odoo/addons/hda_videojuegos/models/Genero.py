
from odoo import models, fields

class Genero(models.Model):
    _name = 'hda_videojuegos.genero'
    _description = 'Genero'

    name = fields.Char('Nombre', required=True)
    description = fields.Char('Descripción')