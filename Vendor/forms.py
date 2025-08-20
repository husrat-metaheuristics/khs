from django import forms
from KHSystemApp.models import *

class VendorForm(forms.ModelForm):

   class Meta:
       model=Vendor
       fields='__all__'

       labels={
             'name':'Vendor Name',
             'ntn':'NTN#',
             'address':'Vendor Address',
             'logo':'Vendor Logo',
       }
