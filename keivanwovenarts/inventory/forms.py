# inventory/forms.py

from django import forms
from .models import Rug, Photo

class RugForm(forms.ModelForm):
    class Meta:
        model = Rug
        fields = ['sku', 'name', 'size', 'age', 'country_of_origin', 'texture', 'style', 'color', 'type', 'price', 'description', 'available']

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'description']

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False)
    sku = forms.CharField(label='SKU', max_length=50, required=False)
    size = forms.CharField(label='Size', max_length=50, required=False)
    age = forms.ChoiceField(label='Age', choices=[('', 'Any')] + Rug.CONDITION_CHOICES, required=False)
    country_of_origin = forms.CharField(label='Country of Origin', max_length=100, required=False)
    texture = forms.ChoiceField(label='Texture', choices=[('', 'Any')] + Rug.TEXTURE_CHOICES, required=False)
    style = forms.ChoiceField(label='Style', choices=[('', 'Any')] + Rug.STYLE_CHOICES, required=False)
    color = forms.CharField(label='Color', max_length=50, required=False)
