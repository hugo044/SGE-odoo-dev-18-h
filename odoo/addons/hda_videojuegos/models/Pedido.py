from odoo import models, fields

class Pedido(models.Model):
    _name = 'hda_videojuegos.pedido'
    _description = 'Pedido'

    codigo = fields.Char('Codigo', required=True)
    description_corta = fields.Char('Descripcion corta')
    
  
    clientes_ids = fields.Many2one('hda_videojuegos.cliente', string='Clientes')