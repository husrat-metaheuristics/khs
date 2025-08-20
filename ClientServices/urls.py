from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.index,name='clientservices_index'),
    path('insert/',views.insert_,name='clientservices_insert'),
    path('<int:id>/',views.insert_,name="clientservices_update"),
    path('delete/<int:id>/',views.delete_,name="clientservices_delete"),
    path('details/<int:id>/',views.details_,name="clientservices_details"),
]