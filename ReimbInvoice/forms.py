from django import forms
from KHSystemApp.models import *

class reimbursementForm(forms.ModelForm):
   class Meta:
      model=Reimbursement
      fields='__all__'
      labels={
              'reInvDate':'Reimbursement Inv Date:',
              'reInvNumber':'Reimbursement Inv #:',
              'invoice':'Select Estimate Title:',
              'notes':'Notes:',
             }


   