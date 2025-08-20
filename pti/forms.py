from KHSystemApp.models import Pti
from django import forms

class PtiForm(forms.ModelForm):
     class Meta:
         model=Pti
         fields='__all__'
         labels={
              'ptiDate':'Pti Date:',
              'invoice':'Select Estimate Title:',
              'deduction':'Deduction If Any:',
              'notes':'Notes:',
             }