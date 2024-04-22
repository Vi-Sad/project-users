from django import forms
from django.core.exceptions import ValidationError

from .models import PersonalInformation


def forbidden_brackets(status):
    brackets = ['{', '}', '[', ']']
    for i in brackets:
        if i in status:
            raise ValidationError('It is forbidden to set these brackets in your status')
    return status


class AddPersonalInformation(forms.ModelForm):
    status = forms.CharField(validators=[forbidden_brackets])

    class Meta:
        model = PersonalInformation
        # fields = '__all__'
        fields = ['status']
        widgets = {
            'status': forms.TextInput(attrs={'name': 'status'})
        }
        required = False
