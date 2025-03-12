from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser


USER_ROLES = [
    ('admin', 'Admin'),
    ('judge', 'Judge'),
    ('participant', 'Participant'),
]

class UserRegistrationForm(UserCreationForm):
    role = forms.ChoiceField(choices=USER_ROLES)


    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'password1', 'password2']
