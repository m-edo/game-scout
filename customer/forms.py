from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User

from customer.models import Profile


class SignUpForm(UserCreationForm):
    username = UsernameField(max_length=30, help_text='Insert your username. 30 characters or fewer. '
                                                      'Letters, digits and @/./+/-/_ only.')
    first_name = forms.CharField(max_length=150, help_text='Insert your first name. 150 characters or fewer.')
    last_name = forms.CharField(max_length=150, help_text='Insert your last name. 150 characters or fewer.')
    email = forms.EmailField(help_text='Insert a valid e-mail address')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email',)
        labels = {'username': 'Username',
                  'first_name': 'First Name',
                  'last_name': 'Last Name',
                  'email': 'E-mail'}


class ChangeProPicForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('picture',)
