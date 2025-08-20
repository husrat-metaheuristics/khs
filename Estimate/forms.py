from django import forms
from KHSystemApp.models import *
from django.contrib.admin.widgets import AdminDateWidget

#Format_Choices=[('Line Numbering','Line Numbering'),('Header Numbering','Header Numbering')]


class EstimateForm(forms.ModelForm):
   
   class Meta:
      model=Estimate
      fields='__all__'
      #estimateFormat=forms.ChoiceField(choices=Format_Choices,widget=forms.RadioSelect())
      labels={
              'estimateGenerationDate':'Estimate Generation Date:',
              'sharedToClientDate':'Shared To Client Date:',
              'reference':'Reference:',
              'description':'Details/Description:',
              'quantity':'Quantity:',
              'rate':'Rate(Rs):',
              'estimateType':'Select Estimate Type?',
              'amount':'Amount(Rs):',
              'invoice':'Estimate Title',
              'estimateFormat':'Select Estimate Format:-',
              'notes':'Notes:',
         }
      widgets={
              'estimateGenerationDate':forms.DateInput(attrs={'type':'date','class':'datepicker','id':'datepicker1'}),
              'sharedToClientDate':forms.DateInput(attrs={'type':'date','class':'datepicker','id':'datepicker'}),
              'description':forms.Textarea(attrs={'type':'textarea','id':'txt-details','readonly':'True','class':'details-txt-area'}),
              'quantity':forms.Textarea(attrs={'type':'textarea','class':'qty-txt-area','id':'txt-qty','readonly':'True'}),
              'rate':forms.Textarea(attrs={'type':'textarea','class':'rate-txt-area','id':'txt-rate','readonly':'True'}),
              'amount':forms.Textarea(attrs={'type':'textarea','class':'amount-txt-area','id':'txt-amount','readonly':'True'}),
        }
