from django.contrib import admin
from django.forms import TextInput, Textarea
from django.template.defaultfilters import truncatechars
from .models import *


@admin.register(Headers, Lets)
class HeadersLetsAdmin(admin.ModelAdmin):
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


@admin.register(Crm)
class CrmAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published']
    list_editable = ['is_published']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': 50})},
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 80})}
    }


@admin.register(Galleries)
class GalleriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'is_published']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': 50})},
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 80})}
    }
    fieldsets = (
        ('Галерея - Текстовая часть', {
            'fields': ('title', 'content')
        }),
        ('Изображение для раздела Django', {
            'fields': ('img_1_dj', 'img_2_dj', 'img_3_dj', 'img_4_dj', 'img_5_dj', 'img_6_dj', 'img_7_dj',
                       'img_8_dj', 'img_9_dj')
        }),
        ('Изображение для раздела Bootstrap', {
            'fields': ('img_1_boots', 'img_2_boots', 'img_3_boots', 'img_4_boots', 'img_5_boots', 'img_6_boots',
                       'img_7_boots', 'img_8_boots', 'img_9_boots')
        }),
        ('Изображение для раздела CSS', {
            'fields': ('img_1_css', 'img_2_css', 'img_3_css', 'img_4_css', 'img_5_css', 'img_6_css', 'img_7_css',
                       'img_8_css', 'img_9_css')
        }),
        ('Опубликовать Галерею', {
            'fields': ('is_published',),
            'description': 'Прежде чем опубликовать второй вариант галереи - убедитесь что у предыдущего варианта '
                           'галереии снято отметка -> ОПУБЛИКОВАНО'
        }),
    )


@admin.register(ReviewsHeader)
class ReviewsHeader(admin.ModelAdmin):
    list_display = ['title', 'title_2', 'is_published']
    list_editable = ['is_published']


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_text', 'created_at', 'is_published']
    list_editable = ['is_published']
    ordering = ['-created_at']
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 80})}
    }

    def short_text(self, obj):
        return truncatechars(obj.text, 30)

    short_text.short_description = 'Отзыв'


@admin.register(FormText)
class FormTextAdmin(admin.ModelAdmin):
    list_display = ['title', 'title2', 'short_content', 'is_published']
    list_editable = ['is_published']

    def short_content(self, obj):
        return truncatechars(obj.content, 30)

    short_content.short_description = 'Контент'


@admin.register(FormQuestions)
class FormQuestionsAdmin(admin.ModelAdmin):
    list_display = ['name', 'questions', 'email', 'created_at']


@admin.register(FooterImages)
class FooterImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published']
    list_editable = ['is_published']


@admin.register(ReviewsAddText)
class ReviewsAddAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published']
    list_editable = ['is_published']
