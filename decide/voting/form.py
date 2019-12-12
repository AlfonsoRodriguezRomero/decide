from django import forms
from .models import Voting

class VotingForm(forms.ModelForm):
    class Meta:
        model = Voting
        fields = ['name','desc','question','auths', 'start_date', 'end_date']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Voting name'}),
            'start_date': forms.DateInput(attrs={'id': 'datetime-local'}),
            'end_date': forms.DateInput(attrs={'id': 'datetime-local-2'})
        }
