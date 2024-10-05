{
    'name': 'Airplanes Management',
    'version': '1.0.0',
    'summary': 'management of airplanes inventory',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/ga_airplane_views.xml',
        'views/ga_airplane_model_views.xml',
        'views/ga_airline_views.xml',
        'views/ga_menus.xml',
    ],
    'installable': True,
    'application': True,
}
