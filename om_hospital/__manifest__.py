# -*- coding: utf-8 -*-
{
    'name': "Hospital Management",

    'summary': """
        Hospital Management System""",

    'description': """
        Hospital Management System
    """,

    'author': "Odoo Mates",
    'category': 'Themes/front',
    'website': "https://www.odoomates.tech",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Hospital',
    'sequence':-100,
    'version': '1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    
    ],
    'aplication':True,
    'auto_install':False,
    'license':'LGPL-3',
}
