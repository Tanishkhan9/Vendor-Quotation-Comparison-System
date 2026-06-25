{
    'name': 'Vendor Quotation Management',

    'version': '18.0.1.0.0',

    'author': 'Tanish Khan',

    'category': 'Purchase',

    'summary': 'Vendor Quotation Comparison System',

    'description': """
Vendor Quotation Management

Features

* Vendor Quotations
* Price Comparison
* Recommendation Engine
* Purchase Analytics
""",

    'depends': [
        'base',
        'purchase',
        'product',
        'mail'
    ],

    'data': [

        'security/ir.model.access.csv',

        'views/menu.xml',

        'views/vendor_quotation_views.xml',

        'views/comparison_views.xml',

    ],

    'application': True,

    'installable': True,

    'auto_install': False,

    'license': 'LGPL-3'
}
