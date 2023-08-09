from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.utils.translation import gettext_lazy as _

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label=_("Nombre"))
    last_name = forms.CharField(label=_("Apellido"))
    email = forms.EmailField(label=_("Correo electrónico"))
    password1 = forms.CharField(label=_("Contraseña"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Confirme contraseña"), widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
        help_texts = { "email": _("Indica un correo electrónico que uses habitualmente"), "first_name": "", "last_name": "", "password1": ""}

class UserEditForm(UserChangeForm):
    first_name = forms.CharField(label=_("Nombre"))
    last_name = forms.CharField(label=_("Apellido"))
    email = forms.EmailField(label=_("Correo electrónico"))

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email"]
        help_texts = { "email": _("Indica un correo electrónico que uses habitualmente"), "first_name": "", "last_name": ""}
