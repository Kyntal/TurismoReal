from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import User

class formLog(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'nombre',
            'apellido', 
            'usuario',  
            'contrasena',
        ]
        labels ={
            'nombre' : 'Nombre',
            'apellido' : 'Primer apellido',   
            'usuario' : 'Nombre de usuario',
            'contrasena' : 'Ingrese Contraseña',
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'class' : 'input-field'}),
            'apellido' : forms.TextInput(attrs={'class' : 'input-field'}),
            'usuario' : forms.TextInput(attrs={'class' : 'input-field'}),
            'contrasena' : forms.TextInput(attrs={'class' : 'input-field'}),
        }

class FormularioLogin(AuthenticationForm):
    class Meta:
        fields = [
                'usuario',  
                'contrasena',
            ]
        labels ={ 
                'usuario' : 'Nombre de usuario',
                'contrasena' : 'Ingrese Contraseña',
            }
        widgets = {
                'usuario' : forms.TextInput(attrs={'class' : 'input-field'}),
                'contrasena' : forms.TextInput(attrs={'class' : 'input-field'}),
            }
            