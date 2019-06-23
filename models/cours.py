# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CoursModel(models.Model):
    _name = 'ecole.cours'
    _description = 'definition de la classe Cours'

    name = fields.Char("Nom")
    code = fields.Char("Code")

