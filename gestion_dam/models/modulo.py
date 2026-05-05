# -*- coding: utf-8 -*-
from odoo import models, fields


class Modulo(models.Model):
    _name = 'dam.modulo'
    _description = 'Módulo DAM'
    _order = 'trimestre, nombre'

    nombre = fields.Char(string='Nombre del módulo', required=True)
    codigo = fields.Char(string='Código', required=True)
    horas = fields.Integer(string='Horas totales')
    trimestre = fields.Selection([
        ('1', '1er Trimestre'),
        ('2', '2º Trimestre'),
        ('3', '3er Trimestre'),
    ], string='Trimestre', required=True, default='1')
    curso = fields.Selection([
        ('1', '1er Curso'),
        ('2', '2º Curso'),
    ], string='Curso', required=True, default='1')
    descripcion = fields.Text(string='Descripción')
    profesor_id = fields.Many2one('dam.profesor', string='Profesor', ondelete='set null')
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_curso', 'En curso'),
        ('superado', 'Superado'),
        ('no_superado', 'No superado'),
    ], string='Estado', default='pendiente')
    nota_final = fields.Float(string='Nota final', digits=(4, 2))
    color = fields.Integer(string='Color')  # para la vista kanban
