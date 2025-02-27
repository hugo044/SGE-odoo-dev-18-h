# -*- coding: utf-8 -*-
{
    'name': "hda_videojuegos",

    'summary': "Modulo sobre la gestion de una tienda de videojuegos",

    'description': """
    Este módulo permite gestionar los clientes, generos, videojuegos y pedidos de una tienda de videojuegos.
    Permite crear, modificar y eliminar componentes en el día a día de una excelente tienda de videojuegos.
    """,

    'author': "Hugo Donoso Aldea",
    'website': "https://www.tiendadevideojuegos.com",
    'icon':'/hda_videojuegos/static/description/icono.png',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/genero.xml',
        'views/menus.xml',
        'views/cliente.xml',
        'views/pedido.xml',
        'views/videojuego.xml',
        'reports/reports.xml',
        'reports/report_videojuego.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

