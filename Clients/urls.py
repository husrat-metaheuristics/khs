from django.urls import path,include
from . import views

urlpatterns=[

    path('',views.index,name='clients_index'),
    path('insert/',views.insert_,name='clients_insert'),
    path('<int:id>/',views.insert_,name="clients_update"),
    path('delete/<int:id>/',views.delete_,name="clients_delete"),
    path('details/<int:id>/',views.details_,name="clients_details"),
]





