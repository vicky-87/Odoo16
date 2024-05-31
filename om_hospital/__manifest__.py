# -*- coding: utf-8 -*-
{
    'name': "Hospital Management",

    'summary': """
        Membuat Module OM Hospital""",

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
    'depends': ['mail', 'product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/patient_tag_data.xml',
        'data/patient.tag.csv',
        'data/sequence_data.xml',
        'wizard/cancel_appointment_view.xml',
        'views/views.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
        'views/patient_tag_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    
    ],
    'aplication':True,
    'auto_install':False,
    'license':'LGPL-3',
}
