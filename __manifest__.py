{
    'name': 'HR recruitment custom',

    'summary': 'Create contact from hr.applicant (web)',

    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'category': 'Human Resources',
    'license': 'Other proprietary',
    'version': '11.0.1.0.1',

    'depends': [
        'contacts',
        'hr_recruitment_survey',
    ],
    'data': [
        'views/survey_user_input_views.xml',
    ],

    'installable': True,
    'application': False,
    'auto_install': False,
}
