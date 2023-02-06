from django import forms
from .models import *

class ModalForm(forms.ModelForm):
    class Meta:
        model = modalidad
        fields = '__all__'
        widgets = {
            'modal':forms.TextInput(attrs={
                'placeholder':'Oferta',
                'class':'form-control'
            })
        }

class OfertaForm(forms.ModelForm):
    class Meta:
        model = oferta
        fields = '__all__'