from django.urls import path,include
from . import views

urlpatterns=[
     path('estimate_insert/',views.estimate_ui,name='estimate_i'),
     path('<int:id>/',views.estimate_ui,name='estimate_u'),
     path('estimate_delete/<int:id>/',views.estimate_d,name='estimate_d'),
     path('estimate_preview/<int:id>/',views.estimate_preview,name='estimate_v'),
     path('estimate_pdf_adv/<int:id>/',views.estimate_pdf_adv,name='estimates_pdf_adv'),
     path('estimate_pdf_rem/<int:id>/',views.estimate_pdf_rem,name='estimates_pdf_rem'),
     path('estimate_v_rem/<int:id>/',views.estimate_v_rem,name='estimate_v_rem'),
      
]