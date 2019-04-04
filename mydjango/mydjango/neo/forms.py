from django import forms

from .models import Neo

class NeoForm(forms.ModelForm):
    name        =forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type in your title'}))
    description =forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder': 'Type in your description'}))
    price       =forms.DecimalField(initial=999)
    class Meta():
        model = Neo
        fields = [
            'name',
            'description',
            'price'
        ]