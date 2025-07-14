from .models import Citation, Source
from django import forms
from django.forms import ModelForm, TextInput, Textarea

class CitationForm(ModelForm):
    class Meta:
        model = Citation
        fields = ['source', 'text']
        widgets = {

            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Цитата'}),
            'source': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Источник'}),

        }
class SourceForm(ModelForm):
    class Meta:
        model = Source
        fields = ['name', 'type']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Источник'}),
            'type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Тип'}),
        }