import unicodedata

from django import forms
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
from django.contrib.auth.forms import UsernameField, AuthenticationForm
from django.contrib.auth.hashers import (
    UNUSABLE_PASSWORD_PREFIX, identify_hasher,
)
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.text import capfirst
from django.utils.translation import gettext, gettext_lazy as _

from .apps import user_registered
from .models import MyUser

UserModel = get_user_model()

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'placeholder': 'password'}),
    )


class RegistrationForm(forms.ModelForm):
    username = UsernameField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}), help_text=password_validation.password_validators_help_text_html)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password again'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'first_name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'last_name'}))




    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError ('Entered passwords are different', code='password_mismatch')}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = False
        user.is_activated = False
        if commit:
            user.save()
        user_registered.send(RegistrationForm, instance=user)
        return user
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'send_messages']