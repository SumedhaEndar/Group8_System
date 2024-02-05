from django import forms
from .models import FitnessProgram
from users.models import Trainer

class FitnessProgramForm(forms.ModelForm):
    program_name = forms.CharField(
        label='Program Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )
    program_day = forms.ChoiceField(
        label='Program Day',
        choices = FitnessProgram.DAYS_OF_WEEK,
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )
    program_time = forms.ChoiceField(
        label='Program Time',
        choices= FitnessProgram.TIME,
        initial='08:00',
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
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

class FitnessProgramEditForm(forms.ModelForm):
    class Meta:
        model = FitnessProgram
        fields = ['program_day','program_time']
        widgets = {
            'program_day': forms.Select(attrs={'class': 'form-control', 'style': 'max-width: 400px;'}),
            'program_time': forms.Select(attrs={'class': 'form-control', 'style': 'max-width: 400px;'}),
        }