from django import forms
from .models import EnglishWord


class WordForm(forms.ModelForm):
    class Meta:
        model = EnglishWord
        fields = ['word', 'translation']
        labels = {'word': '', 'translation': ''}
        widgets = {'word': forms.TextInput(),
                   'translation': forms.TextInput()
                   }


class WordPracticeForm(forms.ModelForm):
    class Meta:
        model = EnglishWord

        fields = ['word', 'translation']
        widgets = {'word': forms.TextInput(),
                   'translation': forms.TextInput()}
