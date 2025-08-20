from django.urls import path,include
from . import views

urlpatterns=[
    #account Header URLS
    path('accountHeaderIndx/',views.ah_index,name='ah_index'),
    path('accountHeaderI/',views.ah_insert,name='ah_I'),
    path('<int:id>/',views.ah_insert,name='ah_U'),
    path('ahDelete/<int:id>/',views.ah_delete,name='ah_del'),
    
    #Petty Cash URLS
    path('',views.pty_index,name='pettycash_index'),
    path('pettyCashI/',views.petty_insert,name='pettycash_I'),
    path('pettycashupdate/<int:id>/',views.petty_insert,name='pettycash_U'),
    path('pettyDelete/<int:id>/',views.petty_delete,name='pettycash_del'),
    path('pettypdf/<int:id>/',views.petty_pdf,name='pettycash_pdf'),
    path('pettycsv/',views.petty_csv,name='pettycash_csv'),   

]