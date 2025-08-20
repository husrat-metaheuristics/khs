from django import forms
from KHSystemApp.models import Invoices,Estimate
from django.contrib.admin.widgets import AdminDateWidget

class InvoicesForm(forms.ModelForm):
    class Meta:
        model=Invoices
        fields='__all__'
        labels={
                 'title':'Invoice/Estimate Title',
                 'fishbowlid':'Fish Bowl Id',
                 'submissionToClientDate':'Submission To Client(Jazz) Date',
                 'vendors':'Select Vendor',
                 'vendorInvoiceId':'Vendor Invoice Id',
                 'clientservices':'Client Services Representative',
                 'taxauthority':'Tax Rate',
                 'client':'Client', 
                 'advancepayment':'Advance Payment(%)',
                 'discountOffered':'Discount Offered',
                 'notes':'Notes:',
           }
        widgets={
                 'submissionToClientDate':forms.DateInput(attrs={'type':'date','class':'datepicker','id':'datepicker','name':'birthday'}),
                 'advancepayment': forms.TextInput(attrs={'type':'range','class':'form-range slider','id':'advancepayment' ,'step': '0.5', 'min': '0', 'max': '100'}),
                 'discountOffered': forms.TextInput(attrs={'type':'range','class':'form-range slider','id':'discountoffered' ,'step': '0.5', 'min': '0', 'max': '100'}),
            }
    def __init__(self,*args,**kwargs):
        super(InvoicesForm,self).__init__(*args,**kwargs)
        self.fields['submissionToClientDate'].widget.attrs['class'] = 'datepicker'
        self.fields['taxauthority'].empty_label="Select Tax Authority"
        self.fields['client'].empty_label="Select Client(Jazz)"
        self.fields['clientservices'].empty_label="Select CS Representative"
        self.fields['vendors'].empty_label="Select Vendor"
