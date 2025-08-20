from django.urls import path,include
from . import views

urlpatterns=[
    path('iportal_insert/',views.iportal_insert,name='iportal_i'),
    path('<int:id>/',views.iportal_insert,name='iportal_u'),
    path('iportalDel/<int:id>/',views.iportal_delete,name='iportal_d'),
    path('iportalDtls/<int:id>/',views.iportal_details,name='iportal_dtls'),
    path('iportalpdf/<int:id>/',views.iportal_pdf,name='iportalpdf'),  
 ]