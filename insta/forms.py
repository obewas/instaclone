from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def ForbiddenUsers(value):
    forbidden_users = ['admin', 'css', 'js', 'authenticate', 'login', 'logout', 'administrator', 'root', 'email', 'user', 'join', 'sql', 'static','python', 'delete']
    if value.lower() in forbidden_users:
        raise ValidationError('Invalid name for user')


def UniqueUser(value):
    if User.objects.filter(username__iexact=value).exists():
        raise ValidationError('User with this username already exists')

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators.append(ForbiddenUsers)
        self.fields['username'].validators.append(UniqueUser)
    def clean(self):
        super(CreateUserForm,self).clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password is confirm_password:
            self.errors['password'] = self.error_class(['Passwords do not match. Try again'])

        return self.cleaned_data




class SearchForm(forms.ModelForm):
    search_query = forms.CharField(max_length=100)


