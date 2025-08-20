from django.urls import path,include
from . import views

urlpatterns=[
     path('estimateType_index/',views.estimateType_idx,name='estimateType_idx'),
     path('estimateType_insert/',views.estimateType_ui,name='estimateType_i'),
     path('<int:id>/',views.estimateType_ui,name='estimateType_u'),
     path('estimateType_delete/<int:id>/',views.estimateType_d,name='estimateType_d'),
]