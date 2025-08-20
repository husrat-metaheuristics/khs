from KHSystemApp.models import PurchaseRequsition
from django import forms

class PrForm(forms.ModelForm):
     class Meta:
         model=PurchaseRequsition
         fields='__all__'
         labels={
              'invoice':'Select Estimate Title:',
              'prRequestedDate':'PR Requested On:',
              'prReceivedDate':'PR Received On:',
              'prNumber':'PR Number:',
             }