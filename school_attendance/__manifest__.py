{
    'name': 'School attendance',
    'version': '1.0',
    'category': 'Education',
    'summary': 'student attendance tracking',
    'depends': ['school_management'],
    'author': 'Tirufat Tesfaye',
    'data': [
        'security/ir.model.access.csv',
        'views/school_attendance_views.xml',
        'views/menu.xml'
    ],
    'application': True,
    'installable': True,
}