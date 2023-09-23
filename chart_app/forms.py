from django import forms
from django.forms import models, NumberInput, FileInput, CharField, Select

from .models import Uploadfiles


class UploadfilesForm(models.ModelForm):
    ex_mov_average = forms.IntegerField(widget=NumberInput(attrs={'placeholder': 'Enter EMA period',
                                                                  'class': 'form-control'}))
    file = forms.FileField(widget=FileInput(attrs={'class': 'form-control'}))
    # timeframe = forms.Select(attrs={'class': 'form-control'})
    class Meta:
        model = Uploadfiles
        fields = ('file', 'timeframe', 'ex_mov_average')
        widgets = {
            'timeframe': forms.Select(attrs={'class': 'form-control'}),
        }