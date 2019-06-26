# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProfesseurModel(models.Model):
    _name = 'ecole.professeur'
    _description = 'definition de la classe Professeur'

    f_name = fields.Char('Nom')
    l_name = fields.Char('Prenom')
    sex = fields.Selection(string='Genre', selection=[('masculin', 'Masculin'), ('feminin', 'Feminin')], )
    cni = fields.Char('Numero CNI', required=True, )
    address = fields.Text('Adresse')
    naissance = fields.Date('Date de Naissance', required=True, )
    start_date = fields.Datetime("Debut de contrat", required=False, default=fields.Datetime.now())
    email = fields.Char()
    phone = fields.Char()
    active = fields.Boolean(string="Actif", )

    departement_id = fields.Many2one(comodel_name="ecole.departement", string="Departement", )
    classe_ids = fields.Many2many(comodel_name="ecole.classe",)
    cours_ids = fields.Many2many(comodel_name="ecole.cours",)


    @api.multi
    def name_get(self):
        result = []
        for professeur in self:
            nam = professeur.f_name + ' ' + professeur.l_name
            result.append((professeur.id, nam))
        return result


    @api.multi
    def send_mail(self):
        self.ensure_one()
        template_id = self.env.ref('ecole.email_template_prof').id
        ctx = {
            'default_model': 'ecole.professeur',
            'default_res_id': self.id,
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'email_to': self.email,
        }
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'target': 'new',
            'context': ctx,
        }
