from django import forms
from .models import Trip

class StartTripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['hora_inicio', 'hora_final']

class EndTripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['distancia', 'dinero']
