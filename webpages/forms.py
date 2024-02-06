from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=255, 
        required=True,
        label='Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'style': 'max-width: 400px;'})
    )
    message = forms.CharField(
        required=True,
        label='Message',
        widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'max-width: 400px; height: 150px;'}),
    )