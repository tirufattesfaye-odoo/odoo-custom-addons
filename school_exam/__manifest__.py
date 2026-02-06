{
    'name': 'School exam',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Core module for School Exam',
    'depends': ['school_management', 'school_academics'],
    'author': 'Tirufat Tesfaye',
    'data': [
            'security/ir.model.access.csv',
            'views/exam_menu.xml',
            'views/exam_views.xml',
            'views/mark_views.xml',
    ],
    'application': True,
    'installable': True,
}