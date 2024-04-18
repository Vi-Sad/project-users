from django import forms
from .models import PersonalInformation


class AddPersonalInformation(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        # fields = '__all__'
        fields = ['status', 'birthday']
        widgets = {
            'birthday': forms.TextInput(attrs={'type': 'date', 'name': 'birthday'}),
            'status': forms.TextInput(attrs={'name': 'status'})
        }
        required = False
