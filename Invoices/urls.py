from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.index,name='invoice_index'),
    path('insert/',views.insert_,name='invoice_insert'),
    path('<int:id>/',views.insert_,name='invoice_update'),
    path('delete/<int:id>/',views.delete_,name='invoice_delete'),
    path('details/<int:id>/',views.details_,name='invoice_details'),
    
 ]