from django.contrib import admin
from .models import *


@admin.register(Headers)
class HeadersAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published']
    list_editable = ['is_published']


@admin.register(Inspires)
class InspiresAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published']
    list_editable = ['is_published']


@admin.register(Lets)
class LetsAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published']
    list_editable = ['is_published']


@admin.register(Crm)
class CrmAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published']
    list_editable = ['is_published']
