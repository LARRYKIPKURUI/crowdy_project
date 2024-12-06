from django.forms import forms
from django import forms
from main_app.models import Fundraiser


class FundraiserForm(forms.ModelForm):
    class Meta:
        model = Fundraiser
        fields = ['first_name', 'last_name', 'email', 'dob', 'gender']
        widgets = {
             'dob' : forms.DateInput(attrs={'type': 'date', 'min':'1980-01-01', 'max':'2005-12-31'}),
        }