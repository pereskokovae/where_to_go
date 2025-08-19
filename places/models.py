from django.db import models


class Place(models.Model):
    title = models.CharField(
        verbose_name='Название места',
        max_length=100,
        db_index=True
        )
    description_short = models.TextField(
        verbose_name='Краткое описание',
        null=True
        )
    description_long = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
        )
    lng = models.DecimalField(
        verbose_name='Долгота',
        max_digits=20,
        decimal_places=18,
        null=True
        )
    lat = models.DecimalField(
        verbose_name='Широта',
        max_digits=20,
        decimal_places=18,
        null=True
        )

    def __str__(self):
        return self.title
