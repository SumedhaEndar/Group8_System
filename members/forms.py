from django import forms
from .models import Member

class MemberUpdateForm(forms.ModelForm):
    phone = forms.CharField(
        max_length=15,
        required=True,
        label='Phone',
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )
    full_name = forms.CharField(
        max_length=100,
        required=True,
        label='Full Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )

    class Meta:
        model = Member
        fields = ['phone', 'full_name']

class PasswordUpdateForm(forms.Form):
    current_password = forms.CharField(
        label='Current Password', 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )
    new_password = forms.CharField(
        label='New Password', 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )
    retype_new_password = forms.CharField(
        label='Retype New Password', 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )