# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ClasseModel(models.Model):
    _name = 'ecole.classe'
    _description = 'definition de la classe classe'
    _inherit = 'mail.thread'

    name = fields.Char("Name")
    code = fields.Char("Code")

    etudiant_ids = fields.One2many(comodel_name="ecole.etudiant", inverse_name="classe_id", string="Etudiants",)
    professeur_ids = fields.Many2many(comodel_name="ecole.professeur",)
    cours_ids = fields.Many2many(comodel_name="ecole.cours",)

    numProf = fields.Integer(string="Nombre de prof", compute='compteur_prof', )
    numCours = fields.Integer(string="Nombre de cours", compute='compteur_cours', )
    numEtudiant = fields.Integer(string="Nombre de d'etutiant", compute='compteur_etudiant', )

    def compteur_prof(self):
        self.numProf = len(self.professeur_ids)

    def compteur_cours(self):
        self.numCours = len(self.cours_ids)

    def compteur_etudiant(self):
        self.numEtudiant = len(self.etudiant_ids)

    @api.onchange('professeur_ids')
    def _onchange_cours_ids(self):
        if len(self.professeur_ids) > 3:
            return {'warning': {'title': 'warning',
                                'message': 'Nombre de professeur atteind'}}
