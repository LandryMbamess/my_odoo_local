# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CoursModel(models.Model):
    _name = 'ecole.cours'
    _description = 'definition de la classe Cours'

    name = fields.Char("Nom")
    code = fields.Char("Code")

    departement_id = fields.Many2one(comodel_name="ecole.departement", string="Departement", )
    classe_ids = fields.Many2many(comodel_name="ecole.classe",)
    professeur_ids = fields.Many2many(comodel_name="ecole.professeur",)
