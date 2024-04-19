import random
from django import forms
from .models import PersonalInformation

personal = PersonalInformation.objects.all()
for i in personal:
    status = i.status
    birthday = i.birthday


class AddPersonalInformation(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        # fields = '__all__'
        fields = ['status', 'birthday']
        widgets = {
            'birthday': forms.TextInput(attrs={'type': 'date', 'name': 'birthday',
                                               'value': f'{birthday.strftime("%Y-%m-%d")}'}),
            'status': forms.TextInput(attrs={'name': 'status', 'value': f'{status}'})
        }
        required = False
