{
    'name': 'Employee Level',
    'version': '16.0.1.0.0',
    'category': 'Sales',
    'sequence': -1,
    'installable': True,
    'application': True,
    'depends': ['base', 'hr', 'stock'],

    'data': [
        'security/ir.model.access.csv',
        'views/employee_view.xml',
        'views/level_changer.xml',
        'views/employee_menu.xml'
    ]

}
