# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EtudiantModel(models.Model):
    _name = 'ecole.etudiant'
    _description = 'definition de la classe Etudiant'

    # name = fields.Char('name', required=True)
    f_name = fields.Char('Nom')
    l_name = fields.Char('Prenom')
    sex = fields.Selection(string='Genre', selection=[('masculin', 'Masculin'), ('feminin', 'Feminin')],)
    cni = fields.Char('Numero CNI', required=True, )
    address = fields.Text('Adresse')
    naissance = fields.Date('Date de Naissance', required=True, )
    inscription = fields.Datetime("Date d'Inscription", required=False, default=fields.Datetime.now())
    email = fields.Char()
    phone = fields.Char()

