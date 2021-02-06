from django.contrib import admin
from django.forms import TextInput, Textarea

from .models import *


@admin.register(Headers)
class HeadersAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published']
    list_editable = ['is_published']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': 50})},
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 80})}
    }


@admin.register(Inspires)
class InspiresAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published']
    list_editable = ['is_published']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': 50})},
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 80})}
    }


@admin.register(Lets)
class LetsAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published']
    list_editable = ['is_published']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': 50})},
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 80})}
    }


@admin.register(Crm)
class CrmAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published']
    list_editable = ['is_published']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': 50})},
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 80})}
    }
