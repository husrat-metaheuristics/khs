from django.urls import path,include
from . import views

urlpatterns=[
    path('assembleEmail_ins/',views.assembleEmail_insert,name='asmEmail_i'),
    path('<int:id>/',views.assembleEmail_insert,name='asmEmail_u'),
    path('assembleEmail_delete/<int:id>/',views.assembleEmail_delete,name='asmEmail_d'),
    path('assembleEmail_details/<int:id>',views.assembleEmail_details,name='asmEmail_details'),
]