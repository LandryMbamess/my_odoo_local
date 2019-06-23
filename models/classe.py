# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ClasseModel(models.Model):
    _name = 'ecole.classe'
    _description = 'definition de la classe classe'

    name = fields.Char("Name")
    code = fields.Char("Code")

    etudiant_ids = fields.One2many(comodel_name="ecole.etudiant", inverse_name="classe_id", string="Etudiants",)
    professeur_ids = fields.Many2many(comodel_name="ecole.professeur",)
    cours_ids = fields.Many2many(comodel_name="ecole.cours",)

