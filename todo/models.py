import datetime
from django.db import models


class User():
    pass


class Task(models.Model):
    title = models.CharField(max_length=250, verbose_name="Titulo")
    message = models.TextField(max_length=400, verbose_name="Descrição")
    conclusion_at = models.DateTimeField(blank=True)
    concluded = models.BooleanField(default=False, verbose_name="Concluído")
    create_at = models.DateTimeField(default=datetime.datetime.now)
    create_by = None

    def __str__(self) -> str:
        return str(self.title + ' create at ' + self.create_at)