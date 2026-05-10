from django import forms
from .models import Fueling

class FuelingForm(forms.ModelForm):
    class Meta:
        model = Fueling
        fields = ['date', 'fuel']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a Date',
                    'type': 'date'
                }
            )
        }