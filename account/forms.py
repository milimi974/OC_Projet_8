from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

User = get_user_model()

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    # Validation password
    def clean_password(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password']:
            raise ValidationError("Password don't match !")


class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        label="Nom",
        widget=forms.TextInput,
        required=True
    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput,
        required=True
    )

    # Validation password
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Cette utilisateur n'existe pas !")
        if not user.check_password(password):
            raise forms.ValidationError("Mot de passe invalid!")
        if not user.is_active:
            raise forms.ValidationError("Le compte utilisateur n'est pas activé.")
        return super(UserLoginForm, self).clean(*args, **kwargs)