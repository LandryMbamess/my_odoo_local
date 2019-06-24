# -*- coding: utf-8 -*-
{
    'name': "Ecole",

    'summary': """
        projet complet d'étude""",

    'description': """
        les debuts
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Project Management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr', 'account', 'project', 'mail',],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/etudiant_vue.xml',
        'views/professeur_vue.xml',
        'views/departement.xml',
        'views/classe.xml',
        'views/cours.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
