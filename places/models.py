from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        verbose_name='Название места',
        max_length=100,
        unique=True
        )
    short_description = models.TextField(
        verbose_name='Краткое описание',
        blank=True
        )
    long_description = HTMLField(
        verbose_name='Описание',
        blank=True
        )
    lng = models.DecimalField(
        verbose_name='Долгота',
        max_digits=20,
        decimal_places=18,
        )
    lat = models.DecimalField(
        verbose_name='Широта',
        max_digits=20,
        decimal_places=18,
        )

    def __str__(self):
        return self.title
    
    class Meta:
        indexes = [models.Index(fields=['title'])]


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name='Место',
        )
    images = models.ImageField(
        verbose_name='Изображение'
        )
    order = models.IntegerField(
        verbose_name='Позиция',
        default=0
        )

    class Meta:
        ordering = ['order']
        unique_together = [['place', 'order']]
        indexes = [models.Index(fields=['order'])]

    def __str__(self):
        return f'{self.order} {self.place.title}'