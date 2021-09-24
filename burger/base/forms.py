
from .models import TopicCategory, Contact
from django import forms

class TopicCategoryForm(forms.ModelForm):
    model = TopicCategory
    exclude = ('fa_class','slug',)

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['ip', 'name', 'email', 'message']