from .models import notitas
from django import forms

class NotitasForm(forms.ModelForm):
    titulo = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), placeholder='Título')
    contenido = forms.Textarea(widget=forms.Textarea(attrs={'class':'form-control'}), placeholder='Contenido')
    
    class Meta:
        model = notitas
        fields = [
            'titulo',
            'contenido',
        ]