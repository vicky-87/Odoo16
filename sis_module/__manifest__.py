# -*- coding: utf-8 -*-
{
    'name': "Sistem Informasi Solusi",

    'summary': """
        Sistem Informasi Solusi (SIS) merupakan sistem informasi yang berisi solusi yang pernah ditawarkan ke calon client ataupun yang telah diimplementasikan oleh client serta teknologi Google Cloud apa saja yang digunakan dalam implementasi tersebut.""",

    'description': """
        Sistem Informasi Solusi (SIS) adalah suatu situs web yang dibuat untuk menyimpan informasi berupa solusi-solusi dan teknologi yang pernah ditawarkan ke calon client ataupun yang telah diimplementasikan oleh client serta informasi singkat mengenai vulnerabilities dan teknologi - teknologi yang ada di Google Cloud. 
        Informasi-informasi tersebut akan digunakan sebagai input dari SIS ini. 
        Dengan adanya sistem ini, pegawai dapat meningkatkan pemahaman mereka akan kemampuan fitur Google Cloud maupun CVE. 
        Pegawai cukup membuka situs web, login ke akunnya, dan mencari hal yang dibutuhkan pada halaman view sebagai output dari sistem ini. 
        Halaman view terdiri dari view available solutions, view available Google Cloud features, dan view common vulnerabilities and exposures.
    """,

    'author': "Kelompok K02-G05 aSIap",
    'website': "https://github.com/rayhankinan/sistem-informasi-solusi",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'module_category_productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/client.xml',
        'views/solution.xml',
        'views/technology.xml',
        'views/vulnerability.xml',
        # 'demo/demo.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
