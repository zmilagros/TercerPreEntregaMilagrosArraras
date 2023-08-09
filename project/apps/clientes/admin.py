from django.contrib import admin
from clientes.models import *
from django.contrib.auth.admin import UserAdmin
from .models import Avatar, CustomUser, Mensajes


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Avatar)
admin.site.register(Mensajes)