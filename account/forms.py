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
    password = forms.CharField(label='Mot de passe',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmer le mot de passe',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    # validate field
    def clean(self, *args, **kwargs):

        #check email
        email = self.cleaned_data.get("email")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Cette email est déjà existant!")

        # check password
        pwd1 = self.cleaned_data.get("password")
        pwd2 = self.cleaned_data.get("password2")
        if pwd1 != pwd2:
            raise forms.ValidationError("les mots de passe ne sont pas identique!")

        return super(UserRegisterForm, self).clean(*args, **kwargs)





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