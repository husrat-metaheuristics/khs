from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.index,name='taxauthority_index'),
    path('insert/',views.insert_,name='taxauthority_insert'),
    path('<int:id>',views.insert_,name='taxauthority_update'),
     path('delete/<int:id>/',views.delete_,name="taxauthority_delete"),
]