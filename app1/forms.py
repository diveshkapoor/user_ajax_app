from django import forms
from app1.models import Person


class UserForm(forms.ModelForm):
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='First name', max_length=100)
    dob = forms.DateField(label='DOB')
    gender = forms.CharField(label='Gender', max_length=1)

    class Meta:
        model = Person
        fields = '__all__'