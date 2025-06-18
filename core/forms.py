from .models import *
from django.forms import ModelForm
from django import forms

class DestinationForm(ModelForm):
    class Meta:
        model = Destination
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter destination name'
            }),
            'weather': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'E.g., Sunny, Rainy, Cold'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City, State or Country'
            }),
            'google_map_link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Paste Google Map URL'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Short description about the place',
                'rows': 3
            }),
        }