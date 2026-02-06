{
    'name': 'School reports',
    'version': '1.0',
    'category': 'Reporting',
    'summary': 'Core module for School Fees',
    'depends': ['school_management', 'school_academics','school_exam','base','web'],
    'author': 'Tirufat Tesfaye',
    'data': [
            'views/wizard_views.xml',
            'reports/report_actions.xml',
            'reports/report_student_card_template.xml',
            'security/ir.model.access.csv',
    ],
    'application': True,
    'installable': True,
}