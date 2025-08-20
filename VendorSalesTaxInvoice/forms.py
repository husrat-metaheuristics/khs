from django import forms
from KHSystemApp.models import Invoices,SalesTaxInvoice
from django.contrib.admin.widgets import AdminDateWidget

class salesTaxInvoiceForm(forms.ModelForm):
    class Meta:
        model=SalesTaxInvoice
        fields='__all__'
        labels={
            'invoice':'Estimate Title.',
            'salesTaxInvoiceRequestedDate':'Sales Tax Invoice Request Date:',
            'salesTaxInvoiceReceivedDate':'Sales Tax Invoice Received Date:',
            'salesTaxFile':'Vendor Sales Tax Invoice',
            'notes':'Notes:',
   
        }