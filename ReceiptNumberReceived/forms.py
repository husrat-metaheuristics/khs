from django import forms
from KHSystemApp.models import Invoices,ReceiptNumberReceived
from django.contrib.admin.widgets import AdminDateWidget

class ReceiptNumberReceivedForm(forms.ModelForm):
    class Meta:
        model=ReceiptNumberReceived
        fields='__all__'
        labels={
            'invoice':'Estimate Title.',
            'receiptReceivedDate':'Receipt Number Received Date:',
            'receiptNumber':'Receipt Number',
            'notes':'Notes:',
        }

   