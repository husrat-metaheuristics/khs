from django.urls import path,include
from . import views

urlpatterns=[
     path('po_insert/',views.po_ui,name='po_i'),
     path('<int:id>/',views.po_ui,name='po_u'),
     path('po_delete/<int:id>/',views.po_d,name='po_d'),
     path('po_preview/<int:id>/',views.po_preview,name='po_preview'),
]