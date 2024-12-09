from django.forms import forms
from django import forms
from main_app.models import Fundraiser, Donation


class FundraiserForm(forms.ModelForm):
    class Meta:
        model = Fundraiser
        fields = ['first_name', 'last_name', 'email', 'dob', 'gender']
        widgets = {
             'dob' : forms.DateInput(attrs={'type': 'date', 'min':'1980-01-01', 'max':'2005-12-31'}),
        }

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['amount','project_name']
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'type': 'number', 'min':'0', 'max':'100000'})
        }