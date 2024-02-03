from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from .models import User, Admin, Trainer, Member
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class TrainerSignUpForm(UserCreationForm):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )
    full_name = forms.CharField(
        label='Full Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )
    phone = forms.CharField(
        label='Phone Number',
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )
    username = forms.CharField(
        label='Username',
        help_text='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )
    trainer_certificate = forms.ImageField(required=False)
    age = forms.IntegerField(
        label='Age',
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )
    bmi = forms.FloatField(
        label='BMI',
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )
    bmr = forms.FloatField(
        label='BMR',
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_trainer = True
        user.is_active = False
        if commit:
            user.save()
        email = user.email
        trainer = Trainer.objects.create(
            user=user, 
            full_name = self.cleaned_data.get('full_name'),
            trainer_certificate = self.cleaned_data.get('trainer_certificate'),
            phone=self.cleaned_data.get('phone'),
            age=self.cleaned_data.get('age'),
            bmi=self.cleaned_data.get('bmi'),
            bmr=self.cleaned_data.get('bmr')
        )
        return user


class MemberSignUpForm(UserCreationForm):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )
    full_name = forms.CharField(
        label='Full Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )
    phone = forms.CharField(
        label='Phone Number',
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )
    username = forms.CharField(
        label='Username',
        help_text='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('full_name', 'username', 'email', 'password1', 'password2')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_member = True
        if commit:
            user.save()
        member = Member.objects.create(
            user=user, 
            full_name=self.cleaned_data.get('full_name'), 
            phone=self.cleaned_data.get('phone')
        )
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )