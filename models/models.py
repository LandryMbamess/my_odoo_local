# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    age = fields.Integer(string="age", )
    description = fields.Char(string="description", )
