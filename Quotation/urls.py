
from django.urls import path,include
from . import views

urlpatterns=[
     path('quo_insert/',views.quo_insert,name='quotation_i'),
     path('<int:id>/',views.quo_insert,name='quotation_u'),
     path('quo_delete/<int:id>/',views.quo_delete,name='quotation_d'),
     path('quo_view/<int:id>/',views.quo_view,name='quotation_v'),
]