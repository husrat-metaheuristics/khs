from django import forms
from KHSystemApp.models import Invoices,JazzReceiptNoRequest
from django.contrib.admin.widgets import AdminDateWidget

class JazzReceiptReqForm(forms.ModelForm):
    class Meta:
        model=JazzReceiptNoRequest
        fields='__all__'
        labels={
            'invoice':'Estimate Title.',
            'receiptReqDate':'Receipt Number Request Date:',
            'notes':'Notes:',
            'initialPtiFile':'Upload PTI',
            'advRiFile':'Upload RI',
        }