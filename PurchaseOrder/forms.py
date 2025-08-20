from KHSystemApp.models import PurchaseOrder
from django import forms

class PoForm(forms.ModelForm):
     class Meta:
         model=PurchaseOrder
         fields='__all__'
         labels={
              'invoice':'Select Estimate Title:',
              'poRequestedDate':'Purchase Order Requested On:',
              'poReceivedDate':'Purchase Order Received On:',
              'poNumber':'Purchase Order #:',
              'poFile':'Browse PO File(pdf):',
              'notes':'Notes:',
             }