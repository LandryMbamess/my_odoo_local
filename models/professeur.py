# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProfesseurModel(models.Model):
    _name = 'ecole.professeur'
    _description = 'definition de la classe Professeur'

    # name = fields.Char('name', required=True)*
    # name = fields.Char(string="nom", required=False, )
    f_name = fields.Char('Nom')
    l_name = fields.Char('Prenom')
    sex = fields.Selection(string='Genre', selection=[('masculin', 'Masculin'), ('feminin', 'Feminin')], )
    cni = fields.Char('Numero CNI', required=True, )
    address = fields.Text('Adresse')
    naissance = fields.Date('Date de Naissance', required=True, )
    start_date = fields.Datetime("Debut de contrat", required=False, default=fields.Datetime.now())
    email = fields.Char()
    phone = fields.Char()

