from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.index,name='vendor_index'),
    path('insert/',views.insert_,name='vendor_insert'),
    path('<int:id>/',views.insert_,name='vendor_update'),
    path('delete/<int:id>/',views.delete_,name='vendor_delete'),
    path('details/<int:id>/',views.details_,name='vendor_details'),
]