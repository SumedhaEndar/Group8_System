from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from .models import User, Admin, Trainer, Member
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class TrainerSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    phone = forms.CharField(max_length=15, required=False)
    trainer_certificate = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_trainer = True
        if commit:
            user.save()
        email = user.email
        trainer = Trainer.objects.create(
            user=user, 
            first_name=self.cleaned_data.get('first_name'), 
            last_name=self.cleaned_data.get('last_name'),
            trainer_certificate = self.cleaned_data.get('trainer_certificate'),
            phone=self.cleaned_data.get('phone')
        )
        return user


class MemberSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    phone = forms.CharField(max_length=15, required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_member = True
        if commit:
            user.save()
        member = Member.objects.create(
            user=user, 
            first_name=self.cleaned_data.get('first_name'), 
            last_name=self.cleaned_data.get('last_name'),
            phone=self.cleaned_data.get('phone')
        )
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())