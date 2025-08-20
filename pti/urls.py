from django.urls import path,include
from . import views

urlpatterns=[
     path('pti_insert/',views.pti_insert,name='pti_i'),
     path('<int:id>/',views.pti_insert,name='pti_u'),
     path('pti_delete/<int:id>/',views.pti_delete,name='pti_d'),
     path('pti_v_rem/<int:id>/',views.pti_preview_rem,name='pti_v_rem'),
     path('pti_v_adv/<int:id>/',views.pti_preview_adv,name='pti_v_adv'),
     path('pti_pdf_rem/<int:id>/',views.pti_pdf_rem,name='pti_pdf_rem'),
     path('pti_pdf_adv/<int:id>/',views.pti_pdf_adv,name='pti_pdf_adv'),
]