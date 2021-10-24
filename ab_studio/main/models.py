from django.db import models

# Create your models here.
from django.urls import reverse


class PhotoInHomePage(models.Model):
    title = models.CharField('Заголовок фотографии', max_length=50)
    description = models.TextField('Описание для фотографии', max_length=254, blank=True)
    photo = models.ImageField('Фотография', upload_to='photo_home')
    text_on_left = models.BooleanField('Текст слева', default=True)


    class Meta:

        verbose_name = 'Фотография на home'
        verbose_name_plural = 'Фотографии на home'

    def __str__(self):

        return self.title

class Album(models.Model):

    title = models.CharField('Заголовок альбома', max_length=50)
    description = models.TextField('Описание альбома', max_length=254, blank=True)
    photo = models.ImageField('Фотография', upload_to='album_presentation')
    is_publish = models.BooleanField('Опубликовать?', default=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Альбом создан')
    slug = models.SlugField(max_length=55, unique=True, db_index=True, verbose_name='URL альбома')

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:album', kwargs={'album_slug': self.slug})



class PhotoAlbums(models.Model):
    photo = models.ImageField('Фотография альбома', upload_to='photo_albums/%Y/%m/%d/')
    album = models.ForeignKey('Album', on_delete=models.CASCADE, verbose_name='Альбом')

    class Meta:
        verbose_name_plural = 'Фотографии альбома'
        verbose_name = 'Фотография альбома'





