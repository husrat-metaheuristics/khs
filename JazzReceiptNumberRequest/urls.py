from django.urls import path,include
from . import views
urlpatterns=[
    path('insert/',views.insert_,name='jazzrecreq_i'),
    path('<int:id>/',views.insert_,name='jazzrecreq_u'),
    path('delete/<int:id>/',views.delete_,name='jazzrecreq_d'),
    path('details/<int:id>/',views.details_,name='jazzrecreq_v'),
    path('pdf/<int:id>/',views.pdf_,name='jazzrecreq_pdf'),
   
 ]
