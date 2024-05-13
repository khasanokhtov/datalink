# datalens_app/forms.py
from django import forms
from .models import Dataset, Data

class DatasetForm(forms.ModelForm):
    class Meta:
        model = Dataset
        fields = ['name', 'description', 'file']  # Поля, которые будут отображаться в форме

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['dataset', 'data_file']
