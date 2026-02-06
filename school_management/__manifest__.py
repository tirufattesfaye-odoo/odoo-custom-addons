{
    'name': 'School Management',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Core module for School Management',
    'depends': ['base','mail','contacts'],
    'author': 'Tirufat Tesfaye',
    'sequence': 1,
    'data': [
        #'security/groups.xml',
        'security/ir.model.access.csv',
        #'security/rules.xml',
        'data/sequence.xml',
        'views/menu.xml',
        'views/academic_year_views.xml',
        'views/student_views.xml',
        'views/guardian_views.xml',
        'views/teacher_views.xml',

    ],
    'application': True,
    'installable': True,
}