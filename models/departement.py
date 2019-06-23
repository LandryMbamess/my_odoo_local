# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DepartementModel(models.Model):
    _name = 'ecole.departement'
    _description = 'definition de la classe departement'

    name = fields.Char("Nom")
    code = fields.Char("Code")

