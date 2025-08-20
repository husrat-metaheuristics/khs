from django.urls import path,include
from . import views 

urlpatterns=[
     path('rnr_insert/',views.rnr_insert_,name='rnr_i'),
     path('<int:id>/',views.rnr_insert_,name='rnr_u'),
     path('rnr_delete/<int:id>/',views.rnr_delete_,name='rnr_d'),
     path('rnr_details/<int:id>/',views.rnr_detail_,name='rnr_detail'),
     path('rnr_pti_receiptnumber/<int:id>/',views.pti_with_receiptnumber,name='pti_receiptnumber')
]