{
    'name': 'Import Order Lines',
    'version': '16.0.1.0.0',
    'category': 'Sales',
    'sequence': -1,
    'installable': True,
    'application': True,
    'depends': ['base', 'sale_management', 'stock'],

    'data': [
        'security/ir.model.access.csv',
        'views/impot_orderline.xml',
        'views/popup_window.xml',

    ]

}
