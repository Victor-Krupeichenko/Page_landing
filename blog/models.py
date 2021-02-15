from django.db import models
from django.urls import reverse_lazy


class Notes(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name='URLs')
    content = models.TextField(verbose_name='Текст статьи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    image = models.ImageField(upload_to='image/notes/%m/%d/', verbose_name='Изображение', blank=True)
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey('BlogCategories', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('views_notes', kwargs={'slug':self.slug})


class BlogCategories(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URLs')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={'slug': self.slug})
