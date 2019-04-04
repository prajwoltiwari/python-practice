from django import forms

from .models import Article

class ArticleModelForm(forms.ModelForm):
    # title =         forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Type in the title of your article.'}))
    # description =   forms.CharField(required = False, widget = forms.Textarea(attrs={'placeholder': 'Type in your Article.'}))
    # summary =       forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Type in the summary.'}))
    class Meta:
        model = Article
        fields = [
            'title',
            'description',
            'summary',
        ]   