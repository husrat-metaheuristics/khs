from django import forms
from KHSystemApp.models import AccountHead,PettyCashEntry


class AccountHeadForm(forms.ModelForm):
    class Meta:
        model=AccountHead
        fields='__all__'
        labels={
            'accountHeadEntranceDate':'Account Head Entrance Date:',
            'accountHeadTitle':'Account Head Title:',
        }


class PettyCashEntryForm(forms.ModelForm):
    class Meta:
        model=PettyCashEntry
        fields='__all__'
        labels={
            'accountHead':'Select Account Head:',
            'pettyCashDate':'Select Date?',
            'narration':'Narration?',
            'branch':'Branch',
            'debt':'Debt Entry',
            'credit':'Credit Entry',
        }
    def __init__(self,*args,**kwargs):
        super(PettyCashEntryForm,self).__init__(*args,**kwargs)
        self.fields['accountHead'].empty_label="Select Account Head"
        

   