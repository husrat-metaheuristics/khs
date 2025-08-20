from django import forms
from KHSystemApp.models import *

class ClientServicesForm(forms.ModelForm):

   class Meta:
       model=ClientServices
       fields='__all__'
       #if you want to load specific fields 
       #fields=('fullname','emp_code','mobile','position' )
       #To rename the labels
       labels= {
               'name':'Full Name',
               'phonenumber':'Phone Number',
               'email':'Email',
               'address':'Address'
              }
       





  