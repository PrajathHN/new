from django import forms
from lawfirmapp.models import LawFirm

class LawFirmForm(forms.ModelForm):
    class Meta:
        model  = LawFirm
        fields = '__all__'