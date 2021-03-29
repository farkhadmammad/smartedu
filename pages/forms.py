from django import forms
from . models import Contact

class ContactForm(forms.ModelForm):
    Ad = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ad'
    }))
    Soyad = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Soyad'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))
    Telefon = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Telefon'
    }))
    mesaj = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Mesaj'
    }))

    class Meta:
        model = Contact
        fields =  ['Ad', 'Soyad', 'email', 'Telefon', 'mesaj']