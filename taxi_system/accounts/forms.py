from django import forms
from .models import Driver
from django.contrib.auth.models import User

class DriverRegistrationForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    telefono=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    no_licencia=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    matricula=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    def clean_username(self):
        username=self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("El nombre de usuario ya está en uso.")
        return username
    def clean_no_licencia(self):
        no_licencia=self.cleaned_data['no_licencia']
        if Driver.objects.filter(No_Licencia=no_licencia).exists():
            raise forms.ValidationError("El número de licencia ya está registrado.")
        return no_licencia