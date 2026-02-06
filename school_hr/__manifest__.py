{
    'name': 'School HR',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'School HR: staff, teachers and assignments',
    'depends': ['school_management', 'hr'],
    'author': 'Tirufat Tesfaye',
    'data': [
        'security/ir.model.access.csv',
        'views/school_hr_views.xml',
        'views/menu.xml',
        #'data/sequence_data.xml',
    ],
    'application': True,
    'installable': True,
}