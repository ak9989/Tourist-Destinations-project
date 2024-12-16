from  django import forms

from .models import Destination


class TouristForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = '__all__'
