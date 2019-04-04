from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    name        =forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type in your title'}))
    description =forms.CharField(required=False, widget=forms.Textarea())
    price       =forms.DecimalField(initial=999)
    class Meta():
        model = Product
        fields = [
            'name',
            'description',
            'price'
        ]

    # def clean_name(self, *args, **kwargs):
    #     name = self.cleaned_data.get('name')
        # if not 'PJ' in name:
        #     raise forms.ValidationError('This is not a valid name')
        # return name


class RawProductForm(forms.Form):
    name        =forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type in your title'}))
    description =forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder':'Type in the description of the form'}))
    price       =forms.DecimalField(initial=999)