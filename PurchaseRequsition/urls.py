from django.urls import path,include
from . import views

urlpatterns=[
     path('pr_insert/',views.pr_ui,name='pr_i'),
     path('<int:id>/',views.pr_ui,name='pr_u'),
     path('pr_delete/<int:id>/',views.pr_d,name='pr_d'),
     path('pr_preview/<int:id>/',views.pr_preview,name='pr_preview'),
]