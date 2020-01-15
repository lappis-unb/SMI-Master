from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import forms
from . import models

from rest_framework import authtoken
from django_cron.models import CronJobLog
from django.contrib.auth.models import Group


class CustomUserAdmin(UserAdmin):
    add_form = forms.CustomUserCreationForm
    form = forms.CustomUserChangeForm
    model = models.CustomUser
    list_display = ['email', 'username', 'user_type']


admin.site.register(models.CustomUser, CustomUserAdmin)

# TODO: find a better place for this
# django_cron package by default register CronJobs on django admin
admin.site.unregister(Group)
admin.site.unregister(CronJobLog)
admin.site.unregister(authtoken.models.Token)
