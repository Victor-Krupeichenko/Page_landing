from django.contrib import admin
from django.template.defaultfilters import truncatechars

from .models import *


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published']
    list_editable = ['is_published']
    # prepopulated_fields = {'slug': ('title',)}


@admin.register(BlogCategories)
class BlogCategoriesAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(CommentNotes)
class CommentNotesAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_text', 'created_at', 'is_published']
    list_editable = ['is_published']

    def short_text(self, obj):
        return truncatechars(obj.text, 20)

    short_text.short_description = 'сообщение'
