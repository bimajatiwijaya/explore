# -*- coding: utf-8 -*-
{
    'name'          : 'Template Report Supplier has not Delivered',
    'version'       : '2.0',
    'summary'       : 'Create Template Report Supplier has not Delivered',
    'sequence'      : 5,
    'description'   : """
    
                        author : Dedy Y 
                        
                        v.1.0 : \n
                        make Template Report Supplier has not Delivered the product for Remainder \n
                        
            
                      """,
    'category'      : 'reports',
    'depends'       : ['base','purchase',],
    'data'          : [
                        'wizard/outstanding_po.xml',
                        'views/purchase_view.xml',
                      ],
    'installable'   : True,
    'application'   : True,
    'auto_install'  : False
}


