from django import forms
from .models import Link 

class AddLinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['url',]
        widgets = {
            'url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Tokopedia Product URL'}),
        }


class EditLinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['url',]
        widgets = {
            'url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Tokopedia Product URL'}),
        }