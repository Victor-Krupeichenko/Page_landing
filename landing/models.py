from django.db import models
from django.urls import reverse_lazy


class Headers(models.Model):
    title = models.CharField(max_length=31, verbose_name='Первый заголовок')
    title_2 = models.CharField(max_length=42, verbose_name='Второй заголовок')
    content = models.TextField(max_length=110, verbose_name='Контентная часть')
    btn_title = models.CharField(max_length=10, default='Читать', blank=True)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовать')

    def __str__(self):
        return self.title


class Inspires(models.Model):
    title = models.CharField(max_length=31, verbose_name='заголовок')
    slug = models.SlugField(max_length=31, unique=True, db_index=True, verbose_name='URLs')
    content = models.TextField(verbose_name='Контент')
    btn_title = models.CharField(max_length=10, default='Читать', blank=True)
    img = models.ImageField(upload_to='images/django/%Y/%m/%d/', verbose_name='Изображение')
    attainment_title = models.CharField(max_length=31, verbose_name='Заголовок')
    attainment_content = models.TextField(max_length=111, verbose_name='Контент')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('single_inspire', kwargs={'slug': self.slug})


class InspireHeader(models.Model):
    title = models.CharField(max_length=31, verbose_name='Первый заголовок')
    title_2 = models.CharField(max_length=42, verbose_name='Второй заголовок')
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Lets(models.Model):
    title = models.CharField(max_length=18, verbose_name='Певый заголовок')
    title_2 = models.CharField(max_length=42, verbose_name='Второй заголовок', blank=True,
                               help_text='Это поле необязательно к заполнению')
    content = models.TextField(verbose_name='Контент')
    slug = models.SlugField(max_length=15, unique=True, db_index=True, verbose_name='URLs')
    btn_title = models.CharField(max_length=10, default='Читать', blank=True)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('single_lets', kwargs={'slug': self.slug})


class Crm(models.Model):
    title = models.CharField(max_length=32, verbose_name='Первый заголовок')
    title_2 = models.CharField(max_length=43, verbose_name='Второй заголовок', blank=True,
                               help_text='Это поле необязательно к заполнению')
    content = models.TextField(max_length=221, verbose_name='Контент')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return self.title


class CrmContent(models.Model):
    title = models.CharField(max_length=14, verbose_name='Заголовок')
    slug = models.SlugField(max_length=14, unique=True, db_index=True, verbose_name='URLs')
    content = models.TextField(verbose_name='Контент')
    img = models.ImageField(upload_to='images/section_crm/%m/%d/', blank=True)
    video = models.TextField(verbose_name='Видео', blank=True,
                             help_text='Это поле необязательно к заполнению')
    crm = models.ForeignKey(Crm, on_delete=models.PROTECT, verbose_name='Блок')
    btn_title = models.CharField(max_length=10, default='Читать', blank=True)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('crm_single', kwargs={'slug': self.slug})


class GalleriesTitles(models.Model):
    title = models.CharField(max_length=32, verbose_name='Заголовок')
    content = models.TextField(max_length=221, verbose_name='Текстовая часть', blank=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class GalleryImages(models.Model):
    title = models.CharField(max_length=32, verbose_name='Название галереи')
    slug = models.SlugField(max_length=32, unique=True, db_index=True, verbose_name='URLs')
    img_1 = models.ImageField(upload_to='images/django/%m/%d/', blank=True, verbose_name='первое изображение')
    img_2 = models.ImageField(upload_to='images/django/%m/%d/', blank=True, verbose_name='второе изображение')
    img_3 = models.ImageField(upload_to='images/django/%m/%d/', blank=True, verbose_name='третья изображение')
    img_4 = models.ImageField(upload_to='images/django/%m/%d/', blank=True, verbose_name='четвёртое изображение')
    img_5 = models.ImageField(upload_to='images/django/%m/%d/', blank=True, verbose_name='пятое изображение')
    img_6 = models.ImageField(upload_to='images/django/%m/%d/', blank=True, verbose_name='шестое изображение')
    img_7 = models.ImageField(upload_to='images/django/%m/%d/', blank=True, verbose_name='седьмое изображение')
    img_8 = models.ImageField(upload_to='images/django/%m/%d/', blank=True, verbose_name='восьмое изображение')
    img_9 = models.ImageField(upload_to='images/django/%m/%d/', blank=True, verbose_name='девятое изображение')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return self.title


class ReviewsHeader(models.Model):
    title = models.CharField(max_length=21, verbose_name='Певый заголовок')
    title_2 = models.CharField(max_length=21, verbose_name='Второй заголовок', blank=True,
                               help_text='Это поле необязательно к заполнению')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return self.title


class Reviews(models.Model):
    name = models.CharField(max_length=11, verbose_name='Имя', help_text='максимальня длина 11 символов')
    text = models.TextField(max_length=170, verbose_name='Отзыв', help_text='максимальня длина 170 символов')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']


class FormText(models.Model):
    title = models.CharField(max_length=15, verbose_name='Первый заголовок')
    title2 = models.CharField(max_length=32, verbose_name='Второй заголовок', blank=True,
                              help_text='Это поле необязательно к заполнению')
    content = models.TextField(max_length=200, verbose_name='Контентная часть', blank=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class FormQuestions(models.Model):
    questions = models.CharField(max_length=150, verbose_name='Вопрос')
    name = models.CharField(max_length=30, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return self.questions


class FooterImages(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название варианта')
    img1 = models.ImageField(upload_to='images_footer/%m/%d/', blank=True)
    img2 = models.ImageField(upload_to='images_footer/%m/%d/', blank=True)
    img3 = models.ImageField(upload_to='images_footer/%m/%d/', blank=True)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return self.title


class ReviewsAddText(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок',
                             help_text='Этот заголовок будет отображатся на странице добовления отзыва')
    img1 = models.ImageField(upload_to='reviews_add/images1/%m/%d/', blank=True)
    img2 = models.ImageField(upload_to='reviews_add/images2/%m/%d/', blank=True)
    img3 = models.ImageField(upload_to='reviews_add/images3/%m/%d/', blank=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
