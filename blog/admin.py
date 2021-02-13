from django.contrib import admin
from .models import *


@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'category', 'photo', 'is_published']
    list_editable = ['is_published']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}
