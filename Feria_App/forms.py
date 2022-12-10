

from tkinter import Widget
from django import forms
from Feria_App.models import Cliente, productor, Transporte
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormularioCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

    
class FormularioProductor(forms.ModelForm):
    class Meta:
        model = productor
        fields = '__all__'


class RegistrarForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Opcional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Opcional.')
    email = forms.EmailField(max_length=254, help_text='Requerido. Informar una dirección de correo electrónico válida.')
    


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )



class TransporteForm(forms.ModelForm):
    class Meta:
        model = Transporte
        fields = '__all__'