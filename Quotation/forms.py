from KHSystemApp.models import Quotation
from django import forms

class QuotationForm(forms.ModelForm):
     class Meta:
         model=Quotation
         fields='__all__'
         labels={
              'quotationReceivedDate':'Quotation Received:',
              'quotationFile':'Browse Quotation File(Pdf):',
              'invoice':'Select Estimate Title:',
              'notes':'Notes:',
             }