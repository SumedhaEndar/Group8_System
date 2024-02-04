from django import forms
from .models import FitnessProgram
from users.models import Trainer

class FitnessProgramForm(forms.ModelForm):
    program_name = forms.CharField(
        label='Program Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )
    program_day = forms.CharField(
        label='Program Day',
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )
    program_time = forms.CharField(
        label='Program Time',
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )
    program_pax = forms.IntegerField(
        label='Program Pax',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )
    program_price = forms.DecimalField(
        label='Program Price',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )
    program_images = forms.ImageField(
        label='Program Images',
        required=True,
        widget=forms.FileInput(attrs={'class': 'form-control-file'})
    )

    class Meta:
        model = FitnessProgram
        fields = ['program_name', 'program_day', 'program_time', 'program_pax', 'program_price', 'program_images']
