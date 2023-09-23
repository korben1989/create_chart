from django import forms
from django.forms import models, FileInput

from .models import Uploadfiles


class UploadfilesForm(models.ModelForm):
    file = forms.FileField(widget=FileInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Uploadfiles
        fields = ('file', 'timeframe', 'ex_mov_average')
        widgets = {
            'timeframe': forms.Select(attrs={'class': 'form-control'}),
            'ex_mov_average': forms.NumberInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Enter EMA period',}),
        }