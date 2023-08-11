from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from productos.models import Producto

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30, verbose_name=_('First name'))
    last_name = models.CharField(max_length=30, verbose_name=_('Last name'))
    email = models.EmailField(unique=True, verbose_name=_('Email'))
    is_active = models.BooleanField(default=True, verbose_name=_('Active'))
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_('Date joined'))

    custom_groups = models.ManyToManyField(Group, related_name='custom_users', blank=True, verbose_name=_('groups'))
    custom_user_permissions = models.ManyToManyField(Permission, related_name='custom_users', blank=True, verbose_name=_('user permissions'))

    def __str__(self):
        return self.username

class Avatar(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    imagen = models.ImageField(
    upload_to='avatares', null=True, blank=True, default="/default.jpeg")
