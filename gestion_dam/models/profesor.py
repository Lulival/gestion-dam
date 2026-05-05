# -*- coding: utf-8 -*-
from odoo import models, fields


class Profesor(models.Model):
    _name = 'dam.profesor'
    _description = 'Profesor DAM'
    _order = 'nombre'

    nombre = fields.Char(string='Nombre completo', required=True)
    email = fields.Char(string='Email')
    telefono = fields.Char(string='Teléfono')
    especialidad = fields.Selection([
        ('programacion', 'Programación'),
        ('bases_datos', 'Bases de Datos'),
        ('sistemas', 'Sistemas'),
        ('interfaces', 'Interfaces'),
        ('otros', 'Otros'),
    ], string='Especialidad', default='programacion')
    activo = fields.Boolean(string='Activo', default=True)
    notas = fields.Text(string='Notas')

    # Relación inversa: módulos que imparte este profesor
    modulo_ids = fields.One2many('dam.modulo', 'profesor_id', string='Módulos que imparte')
    modulos_count = fields.Integer(string='Nº de módulos', compute='_compute_modulos_count')

    def _compute_modulos_count(self):
        for record in self:
            record.modulos_count = len(record.modulo_ids)
