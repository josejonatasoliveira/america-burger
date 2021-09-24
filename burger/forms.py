
from django import forms
from burger.enumarations import ALL_LANGUAGES

class BaseForm(forms.Form):
    LANGUAGES = (('', '--------'),) + ALL_LANGUAGES
    language = forms.ChoiceField(
        required=False,
        choices=LANGUAGES,
    )
    keywords = forms.CharField(required=False)