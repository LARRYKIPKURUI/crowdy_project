from django.forms import forms
from django import forms
from main_app.models import Fundraiser, Donation


class FundraiserForm(forms.ModelForm):
    class Meta:
        model = Fundraiser
        fields = ['first_name', 'last_name', 'email', 'dob', 'gender']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date', 'min': '1980-01-01', 'max': '2005-12-31'}),
        }


class DonationForm(forms.ModelForm):
    project_name = forms.ChoiceField(
        label='Project Name',
        choices=(
            ('', 'Select Project'),
            ('estate_road_renovation', 'Estate Road Renovation'),
            ('community_borehole', 'Community Borehole'),
            ('public_park_clean_up', 'Public Park Clean Up'),
            ('community_college_construction', 'Community College Construction'),
        ),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True,  # Make the field required
    )

    class Meta:
        model = Donation
        fields = ['amount', 'project_name']
        widgets = {
            'amount': forms.NumberInput(attrs={'type': 'number', 'min': '0', 'max': '100000'}),
        }
