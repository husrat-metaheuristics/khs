
from django import forms
from KHSystemApp.models import *

class TaxAuthorityForm(forms.ModelForm):

   class Meta:
         model=TaxAuthority
         #fields=['taxauthority']
         fields='__all__'
        # exclude=('taxrate',)
         labels= {
               'taxauthority':'Tax Authority',
               'taxrate':'Tax Rate',
               'isReimbursed':'Is It Reimbursement Case',
              }
         widgets = {
                 'taxrate': forms.TextInput(attrs={'type':'range','class':'form-range slider','id':'myRange' ,'step': '0.5', 'min': '0', 'max': '100'})
              }