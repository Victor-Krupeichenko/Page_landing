from django.db import models


class Headers(models.Model):
    title = models.CharField(max_length=31, verbose_name='Первый заголовок')
    title_2 = models.CharField(max_length=42, verbose_name='Второй заголовок')
    content = models.TextField(max_length=110, verbose_name='Контентная часть')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовать')

    def __str__(self):
        return self.title


class Inspires(models.Model):
    title = models.CharField(max_length=31, verbose_name='Первый заголовок')
    title_2 = models.CharField(max_length=42, verbose_name='Второй заголовок')
    django_content = models.TextField(max_length=281, verbose_name='Контент Django')
    bootstrap_content = models.TextField(max_length=281, verbose_name='Контент Bootstrap')
    css_content = models.TextField(max_length=281, verbose_name='Контент CSS')
    django_img = models.ImageField(upload_to='images/django/%Y/%m/%d/', blank=True, verbose_name='Изображение',
                                   help_text='Это поле необязательно к заполнению')
    bootstrap_img = models.ImageField(upload_to='images/bootstrap/%Y/%m/%d/', blank=True, verbose_name='Изображение',
                                      help_text='Это поле необязательно к заполнению')
    css_img = models.ImageField(upload_to='images/css/%Y/%m/%d/', blank=True, verbose_name='Изображение',
                                help_text='Это поле необязательно к заполнению')
    attainment_django_num = models.CharField(max_length=7, verbose_name='Достижение в цифрах')
    attainment_django_title = models.CharField(max_length=31, verbose_name='Заголовок')
    attainment_django_content = models.TextField(max_length=111, verbose_name='Контент')
    attainment_bootstrap_num = models.CharField(max_length=7, verbose_name='Достижение в цифрах')
    attainment_bootstrap_title = models.CharField(max_length=31, verbose_name='Заголовок')
    attainment_bootstrap_content = models.TextField(max_length=111, verbose_name='Контент')
    attainment_css_num = models.CharField(max_length=7, verbose_name='Достижение в цифрах')
    attainment_css_title = models.CharField(max_length=31, verbose_name='Заголовок')
    attainment_css_content = models.TextField(max_length=111, verbose_name='Контент')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return self.title


class Lets(models.Model):
    title = models.CharField(max_length=18, verbose_name='Певый заголовок')
    title_2 = models.CharField(max_length=42, verbose_name='Второй заголовок', blank=True,
                               help_text='Это поле необязательно к заполнению')
    lets_content = models.TextField(max_length=171, verbose_name='Контент')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return self.title


class Crm(models.Model):
    title = models.CharField(max_length=32, verbose_name='Первый заголовок')
    title_2 = models.CharField(max_length=43, verbose_name='Второй заголовок', blank=True,
                               help_text='Это поле необязательно к заполнению')
    content = models.TextField(max_length=221, verbose_name='Контент')
    section_1 = models.CharField(max_length=14, verbose_name='Заголовок')
    section_content = models.TextField(max_length=110, verbose_name='Контент')
    section_2 = models.CharField(max_length=14, verbose_name='Заголовок')
    section_2_content = models.TextField(max_length=110, verbose_name='Контент')
    video_1 = models.TextField(verbose_name='Видео', blank=True,
                               help_text='Это поле необязательно к заполнению')
    video_2 = models.TextField(verbose_name='Видео', blank=True,
                               help_text='Это поле необязательно к заполнению')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return self.title
