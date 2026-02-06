{
    'name': 'School fees Management',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Core module for School Fees',
    'depends': ['school_management', 'account'],
    'author': 'Tirufat Tesfaye',
    'data': [
        'views/menu.xml',
        'views/school_fees_views.xml',
        'security/ir.model.access.csv',

    ],
    'application': True,
    'installable': True,
}