# -*- coding: utf-8 -*-

from odoo import models, fields

class Autor(models.Model):
    _name = 'sge_libreria.autor'
    _description = 'Autor'

    name = fields.Char('Nombre', required=True)
    fecha_nac = fields.Char('Fecha de nacimiento')

    country_id = fields.Many2one('res.country', string='Pais de origen')