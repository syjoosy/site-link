from django import forms
from .models import Link

class CreateLink(forms.ModelForm):
    long_link = forms.CharField(label='Длинная ссылка:',
                                 widget=forms.TextInput(attrs={'placeholder': 'Введите ссылку'}))
    short_link = forms.CharField(label='Сокращенная ссылка:',
                                 widget=forms.TextInput(attrs={'placeholder': 'Введите слово сокращение'}))

    class Meta:
        model = Link
        fields = ['long_link', 'short_link']
