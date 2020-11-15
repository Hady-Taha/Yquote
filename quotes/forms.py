from django import forms
from .models import Quote
# Create your forms here.


class AddNewQoute(forms.ModelForm):
    class Meta:
        model=Quote
        fields=('qoute',)

    qoute=forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'form-control rounded-pill','placeholder':'Your Qoute...✍'}
            ))

    pass