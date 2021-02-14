from django.contrib import admin
from .models import *


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published']
    list_editable = ['is_published']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(BlogCategories)
class BlogCategoriesAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}
