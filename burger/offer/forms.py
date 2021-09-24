from django import forms
from .models import Offer

class OfferForm(forms.ModelForm):

    class Meta:
        model = Offer
        exclude = ('id_hash', 'upload_session','slug',)

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        if end_date < start_date:
            raise forms.ValidationError("End date should be greater than start date.")