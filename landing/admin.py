from django.contrib import admin
from django.forms import TextInput, Textarea
from django.template.defaultfilters import truncatechars
from .models import *


@admin.register(Headers)
class HeadersLetsAdmin(admin.ModelAdmin):
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
    prepopulated_fields = {'slug': ('content',)}


@admin.register(Inspires)
class InspiresAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published']
    list_editable = ['is_published']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': 50})},
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 80})}
    }
    prepopulated_fields = {'slug': ('title',)}


@admin.register(InspireHeader)
class InspireHeaderAdmin(admin.ModelAdmin):
    list_display = ['title', 'title_2', 'is_published']
    list_editable = ['is_published']


@admin.register(Crm)
class CrmAdmin(admin.ModelAdmin):
    list_display = ['title', 'title_2', 'short_content', 'is_published']
    list_editable = ['is_published']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': 50})},
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 80})}
    }

    def short_content(self, obj):
        return truncatechars(obj.content, 30)

    short_content.short_description = 'Контент'


@admin.register(CrmContent)
class CrmContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_content', 'is_published']
    list_editable = ['is_published']

    def short_content(self, odj):
        return truncatechars(odj.content, 30)

    short_content.short_description = 'контент'

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': 50})},
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 80})}
    }
    prepopulated_fields = {'slug': ('title',)}


@admin.register(GalleriesTitles)
class GalleriesTitlesAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_content', 'is_published']
    list_editable = ['is_published']

    def short_content(self, odj):
        return truncatechars(odj.content, 30)

    short_content.short_description = 'контент'

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': 50})},
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 80})}
    }


@admin.register(GalleryImages)
class GalleryImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published']
    list_editable = ['is_published']
    prepopulated_fields = {'slug': ('title',)}


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
