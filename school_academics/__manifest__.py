{
    'name': 'School academics',
    'version': '1.0',
    'category': 'Education',
    'summary': 'academic years, timetables and enrollments',
    'depends': ['base', 'school_management'],
    'author': 'Tirufat Tesfaye',
    'data': [
        'security/ir.model.access.csv',
        'views/academic_year_views.xml',
        'views/timetable_views.xml',
        'views/academic_term_views.xml',
        'views/course_views.xml',
        'views/menu_views.xml',
        'views/subject_views.xml',

    ],
    'application': True,
    'installable': True,
}