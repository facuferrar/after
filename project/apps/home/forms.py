from django import forms
from .models import Modelo1, Modelo2, Modelo3, Modelo4

class MyForm(forms.Form):
    campo1 = forms.CharField(max_length=100)
    campo2 = forms.IntegerField()
    campo3 = forms.CharField(max_length=100)
    campo4 = forms.IntegerField()
    campo5 = forms.CharField(max_length=100)
    campo6 = forms.IntegerField()
    campo7 = forms.CharField(max_length=100)
    campo8 = forms.IntegerField()

