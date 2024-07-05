from django.db import models

# Create your models here.
class Film_comment(models.Model):
    title = models.CharField('Название фильма', max_length=100)
    description = models.TextField('Описание фильма')
    comment = models.TextField('Комментарий к фильму')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.title

class Add_film(models.Model):
    film_title = models.CharField('Название фильма', max_length=100)
    film_description = models.TextField('Описание фильма')
    image = models.ImageField('Изображение', upload_to='films/img')

    class Meta:
        verbose_name = 'Добавить фильм'
        verbose_name_plural = 'Добавить фильмы'

    def __str__(self):
        return self.title