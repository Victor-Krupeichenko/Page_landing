from django.db import models
from django.urls import reverse_lazy


class Headers(models.Model):
    title = models.CharField(max_length=31, verbose_name='Первый заголовок')
    title_2 = models.CharField(max_length=42, verbose_name='Второй заголовок')
    content = models.TextField(max_length=110, verbose_name='Контентная часть')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовать')

    def __str__(self):
        return self.title


class Inspires(models.Model):
    title = models.CharField(max_length=31, verbose_name='заголовок')
    slug = models.SlugField(max_length=31, unique=True, db_index=True, verbose_name='URLs')
    content = models.TextField( verbose_name='Контент')
    img = models.ImageField(upload_to='images/django/%Y/%m/%d/', blank=True, verbose_name='Изображение',
                                   help_text='Это поле необязательно к заполнению')
    attainment_title = models.CharField(max_length=31, verbose_name='Заголовок')
    attainment_content = models.TextField(max_length=111, verbose_name='Контент')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('single_inspire', kwargs={'slug':self.slug})

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


class Galleries(models.Model):
    title = models.CharField(max_length=32, verbose_name='Заголовок')
    content = models.TextField(max_length=221, verbose_name='Текстовая часть', blank=True)
    img_1_dj = models.ImageField(upload_to='images/django/%m/%d/', blank=True, verbose_name='первое изображение')
    img_2_dj = models.ImageField(upload_to='images/django/%m/%d/', blank=True, verbose_name='второе изображение')
    img_3_dj = models.ImageField(upload_to='images/django/%m/%d/', blank=True, verbose_name='третья изображение')
    img_4_dj = models.ImageField(upload_to='images/django/%m/%d/', blank=True, verbose_name='четвёртое изображение')
    img_5_dj = models.ImageField(upload_to='images/django/%m/%d/', blank=True, verbose_name='пятое изображение')
    img_6_dj = models.ImageField(upload_to='images/django/%m/%d/', blank=True, verbose_name='шестое изображение')
    img_7_dj = models.ImageField(upload_to='images/django/%m/%d/', blank=True, verbose_name='седьмое изображение')
    img_8_dj = models.ImageField(upload_to='images/django/%m/%d/', blank=True, verbose_name='восьмое изображение')
    img_9_dj = models.ImageField(upload_to='images/django/%m/%d/', blank=True, verbose_name='девятое изображение')
    img_1_boots = models.ImageField(upload_to='images/bootstrap/%m/%d/', blank=True, verbose_name='первое изображение')
    img_2_boots = models.ImageField(upload_to='images/bootstrap/%m/%d/', blank=True, verbose_name='второе изображение')
    img_3_boots = models.ImageField(upload_to='images/bootstrap/%m/%d/', blank=True, verbose_name='третье изображение')
    img_4_boots = models.ImageField(upload_to='images/bootstrap/%m/%d/', blank=True,
                                    verbose_name='четвертое изображение')
    img_5_boots = models.ImageField(upload_to='images/bootstrap/%m/%d/', blank=True, verbose_name='пятое изображение')
    img_6_boots = models.ImageField(upload_to='images/bootstrap/%m/%d/', blank=True, verbose_name='шестое изображение')
    img_7_boots = models.ImageField(upload_to='images/bootstrap/%m/%d/', blank=True, verbose_name='седьмое изображение')
    img_8_boots = models.ImageField(upload_to='images/bootstrap/%m/%d/', blank=True, verbose_name='восьмое изображение')
    img_9_boots = models.ImageField(upload_to='images/bootstrap/%m/%d/', blank=True, verbose_name='девятое изображение')
    img_1_css = models.ImageField(upload_to='images/css/%m/%d/', blank=True, verbose_name='первое изображение')
    img_2_css = models.ImageField(upload_to='images/css/%m/%d/', blank=True, verbose_name='второе изображение')
    img_3_css = models.ImageField(upload_to='images/css/%m/%d/', blank=True, verbose_name='третье изображение')
    img_4_css = models.ImageField(upload_to='images/css/%m/%d/', blank=True, verbose_name='четвертое изображение')
    img_5_css = models.ImageField(upload_to='images/css/%m/%d/', blank=True, verbose_name='пятое изображение')
    img_6_css = models.ImageField(upload_to='images/css/%m/%d/', blank=True, verbose_name='шестое изображение')
    img_7_css = models.ImageField(upload_to='images/css/%m/%d/', blank=True, verbose_name='седьмое изображение')
    img_8_css = models.ImageField(upload_to='images/css/%m/%d/', blank=True, verbose_name='восьмое изображение')
    img_9_css = models.ImageField(upload_to='images/css/%m/%d/', blank=True, verbose_name='девятое изображение')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return self.title


class ReviewsHeader(models.Model):
    title = models.CharField(max_length=16, verbose_name='Певый заголовок')
    title_2 = models.CharField(max_length=16, verbose_name='Второй заголовок', blank=True,
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
