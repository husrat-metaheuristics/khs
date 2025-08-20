from django.urls import path,include
from . import views

urlpatterns=[
     path('reimb_insert/',views.reimb_insert,name='reimb_i'),
     path('<int:id>/',views.reimb_insert,name='reimb_u'),
     path('reimb_delete/<int:id>/',views.reimb_delete,name='reimb_d'),
     path('reimb_view_adv/<int:id>/',views.reimb_preview_adv,name='reimb_v_adv'),
     path('reimb_view_rem/<int:id>/',views.reimb_preview_rem,name='reimb_v_rem'),
     path('reimbursement_pdf_adv/<int:id>',views.ri_pdf_adv,name='reimb_pdf_adv'),
     path('reimbursement_pdf_rem/<int:id>',views.ri_pdf_rem,name='reimb_pdf_rem'),

]