from django import forms
from asosiy.models import *

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['kim', 'ozi_haqida']

class TajribaForm(forms.ModelForm):
    class Meta:
        model = Tajriba
        fields = ['kompaniya', 'yil', 'kim']


class MalakaForm(forms.ModelForm):
    class Meta:
        model = Malaka
        fields = ['nomi', 'daraja']


class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = ['name', 'link1', 'link2']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingiz'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Xabar'}),
        }
