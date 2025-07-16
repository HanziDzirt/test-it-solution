from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Source(models.Model):
    name = models.CharField('Источник', max_length=120)
    type = models.CharField('Тип', max_length=20, choices=[('movie', 'Фильм'), ('book', 'Книга')])

    def __str__(self):
        type_display = dict(self._meta.get_field('type').choices).get(self.type, self.type)
        return f"{self.name} ({type_display})"

class Citation(models.Model):
    text = models.TextField('Текст', unique=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    weight = models.FloatField('Вес', default=1)
    likes = models.IntegerField('Лайки', default=0)
    dislikes = models.IntegerField('Дизлайки', default=0)
    views = models.PositiveIntegerField('Просмотры', default=0)
    def __str__(self):
        return f"{self.source.name}, ({self.source.get_type_display()})"