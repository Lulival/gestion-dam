# -*- coding: utf-8 -*-
{
    'name': 'Gestión DAM',
    'version': '1.0',
    'summary': 'Gestor de módulos y profesores del ciclo DAM',
    'description': """
        Módulo para gestionar las asignaturas y profesores
        del ciclo formativo de Desarrollo de Aplicaciones Multiplataforma (DAM).
    """,
    'category': 'Education',
    'author': 'Lucila',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/profesor_views.xml',
        'views/modulo_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
