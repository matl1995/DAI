from django import forms
from .validators import valida_codigo_postal

class RestauranteForm(forms.Form):
    borough = forms.CharField(label='', max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Bronx'}))

class ModificarForm(forms.Form):
    ident = forms.CharField(label='', max_length=20, required=False, widget = forms.HiddenInput())
    name = forms.CharField(label='Nombre', max_length=21, required=False)
    borough = forms.CharField(label='Barrio', max_length=20, required=False)
    cuisine = forms.CharField(label='Cocina', max_length=20, required=False)
    lat = forms.CharField(label='', max_length=20, required=False, widget = forms.HiddenInput())
    lon = forms.CharField(label='', max_length=20, required=False, widget = forms.HiddenInput())

class AniadirForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=20, required=True)
    borough = forms.CharField(label='Barrio', max_length=20, required=True)
    cuisine = forms.CharField(label='Cocina', max_length=20, required=True)
    zipcode = forms.IntegerField(label='Código Postal',validators=[valida_codigo_postal], required=True)