# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ClasseModel(models.Model):
    _name = 'ecole.classe'
    _description = 'definition de la classe classe'

    name = fields.Char("Nom")
    code = fields.Char("Code")

