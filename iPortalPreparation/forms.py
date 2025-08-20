from django import forms
from KHSystemApp.models import Invoices,iPortalPreparation
from django.contrib.admin.widgets import AdminDateWidget

class iPortalPreparationForm(forms.ModelForm):
    class Meta:
        model=iPortalPreparation
        fields='__all__'
        labels={
            'invoice':'Estimate Title.',
            'uploadedDate':'iPortal Uploaded Date:',
            'ptiPdfFile':'Upload PTI',
            'riPdfFile':'Upload RI',
            'notes':'Notes:',
        }