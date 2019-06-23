# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DepartementModel(models.Model):
    _name = 'ecole.departement'
    _description = 'definition de la classe departement'

    name = fields.Char("Nom")
    code = fields.Char("Code")

    professeur_ids = fields.One2many(comodel_name="ecole.professeur", inverse_name="departement_id",
                                     string="Professeurs", )
    cours_ids = fields.One2many(comodel_name="ecole.professeur", inverse_name="departement_id", string="Cours",)


