from django.urls import path,include
from . import views

urlpatterns=[
     path('sales_tax_insert/',views.sales_tax_ui,name='sales_tax_i'),
     path('<int:id>/',views.sales_tax_ui,name='sales_tax_u'),
     path('salestax_delete/<int:id>/',views.sales_tax_d,name='sales_tax_d'),
     path('salestax_detail/<int:id>/',views.sales_tax_details,name='sales_tax_det'),
     path('backToInvoices/',views.back_to_invoices,name='back_to_projects'),
]