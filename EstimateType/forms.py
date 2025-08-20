from django import forms
from KHSystemApp.models import *

class estimateTypeForm(forms.ModelForm):
   class Meta:
       model=EstimateType
       fields='__all__'
       labels= {
               'EstimateTypeTitle':'Estimate Type Title',
               'isTaxable':'Is The Estimate Type Taxable?',
              }