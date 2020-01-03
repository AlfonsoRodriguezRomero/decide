from django import forms
from .models import Voting

class VotingForm(forms.ModelForm):
    class Meta:
        model = Voting
        fields = ['name','desc','questions','auths']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Voting name'}),
            
            
        }