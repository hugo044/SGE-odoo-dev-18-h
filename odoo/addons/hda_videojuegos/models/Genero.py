
from odoo import models, fields

class Genero(models.Model):
    _name = 'hda_videojuegos.genero'
    _inherit = ['mail.thread' , 'mail.activity.mixin']
    _description = 'Genero'

    name = fields.Char('Nombre', required=True,help="Introduzca el nombre de la categoria")
    description = fields.Char('Descripción', help="Introduzca una descripcion a la categoria")
    
    videojuego_ids = fields.Many2many('hda_videojuegos.videojuego', relation="hda_videojuegos_genero_videojuego_rel" , string='Videojuego')

    def enviar_notificacion(self):
        self.message_post(body="Se ha realizado un cambio importante",
                            subtype_id=self.env.ref('mail.mt_note').id)