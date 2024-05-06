from django import forms
from django.forms import BooleanField

from catalog.models import Product, Version

forbidden_words = ['казино',
                   'криптовалюта',
                   'крипта',
                   'биржа',
                   'дешево',
                   'бесплатно',
                   'обман',
                   'полиция',
                   'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('owner', 'created_at', 'updated_at')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for word in forbidden_words:
            if word.lower() in cleaned_data.lower():
                raise forms.ValidationError('Наименование не должно содержать запрещённых слов')
            else:
                return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        if cleaned_data.lower() in forbidden_words:
            raise forms.ValidationError('Описание не должно содержать запрещённых слов')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for word in forbidden_words:
            if word.lower() in cleaned_data.lower():
                raise forms.ValidationError('Название не должно содержать запрещённых слов')
            else:
                return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        if cleaned_data.lower() in forbidden_words:
            raise forms.ValidationError('Описание не должно содержать запрещённых слов')
        return cleaned_data
