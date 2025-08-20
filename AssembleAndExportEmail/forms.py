from django import forms
from KHSystemApp.models import *

class AssembleExportEmailForm(forms.ModelForm):
   class Meta:
       model=AssembleExportEmail
       fields='__all__'
       labels= {
               'invoice':'Select Project?',
               'emailText':'Paste Email Text',
               'emailsPdfFile':'All Emails Pdf',
              }