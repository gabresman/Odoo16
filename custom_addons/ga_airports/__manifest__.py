{
    'name': 'Airports Management',
    'version': '1.0.0',
    'summary': 'management of airports',
    'depends': [
        'base',
        'ga_navega',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/ga_airport_views.xml',
        'views/ga_menus.xml',
    ],
    'installable': True,
    'application': True,
}
