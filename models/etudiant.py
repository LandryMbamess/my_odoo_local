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

    state = fields.Selection(string="Niveau", selection=[('L1', 'Licence 1'), ('L2', 'Licence 2'), ('L3', 'Licence 2'),
                                                         ('Fin', 'Fin'), ],)

    departement_id = fields.Many2one(comodel_name="ecole.departement", string="Departement", )
    classe_id = fields.Many2one(comodel_name="ecole.classe", string="Classe", )

    cours_ids = fields.Many2many(related='classe_id.cours_ids')  # relation d'une classe à une autre

    @api.multi
    def name_get(self):
        result = []
        for etudiant in self:
            name = etudiant.f_name + ' ' + etudiant.l_name
            result.append((etudiant.id, name))
        return result
    #
    # @api.constrains('naissance', 'inscription')
    # def chek_date(self):
    #     if self.naissance > self.inscription:
    #       raise ValueError('la date de naissance ne peut pas être grande que la dacte actuelle entrer la bonne date')
    #
