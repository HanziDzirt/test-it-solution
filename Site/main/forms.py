from .models import Citation, Source
from django import forms
from django.forms import ModelForm, TextInput, Textarea,  NumberInput

class CitationForm(ModelForm):
    class Meta:
        model = Citation
        fields = ['source', 'text', 'weight']
        widgets = {
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Цитата'}),
            'source': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Источник'}),
            'weight': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Вес', 'min': 0.1, 'step': 0.1}),
        }


class SourceForm(ModelForm):
    class Meta:
        model = Source
        fields = ['name', 'type']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Источник'}),
            'type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Тип'}),
        }
