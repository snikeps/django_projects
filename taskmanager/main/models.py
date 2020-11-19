from django.db import models


class Task(models.Model):
    title = models.CharField('Task_name', max_length=50)
    task = models.TextField('Descripton')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tassk'
        verbose_name_plural  = 'Tassks'