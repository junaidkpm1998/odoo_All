{
    'name': 'Package in SO',
    'version': '16.0.1.0.0',
    'category': 'Sales',
    'sequence': -16,
    'installable': True,
    'application': True,
    'depends': ['base', 'sale_management', 'stock'],

    'data': [

        'security/ir.model.access.csv',
        'views/package_views.xml',
        'views/sale_xpath.xml',
        'views/package_bundle.xml',
        'views/detail_view.xml',
        'views/package_menu_action.xml',

    ]

}