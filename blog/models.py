from django.db import models


class Blogs(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок статьи')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URl-slug')
    content = models.TextField(verbose_name='Текст статьи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редакирования')
    photo = models.ImageField(upload_to='photo/blog/%m/%d/', blank=True, verbose_name='Фото')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, verbose_name='Категория')

    class Meta:
        ordering =['-created_at']

    def __str__(self):
        return self.title


class Categories(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название категории')
    slug = models.SlugField(max_length=20, unique=True, db_index=True, verbose_name='URl-slug')

    def __str__(self):
        return self.title
