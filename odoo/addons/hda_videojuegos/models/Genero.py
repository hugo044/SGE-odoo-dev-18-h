
from odoo import models, fields

class Genero(models.Model):
    _name = 'hda_videojuegos.genero'
    _inherit = ['mail.thread' , 'mail.activity.mixin']
    _description = 'Genero'

    name = fields.Char('Nombre', required=True, tracking=True)
    description = fields.Char('Descripción')

    def enviar_notificacion(self):
        self.message_post(body="Se ha realizado un cambio importante",
                            subtype_id=self.env.ref('mail.mt_note').id)