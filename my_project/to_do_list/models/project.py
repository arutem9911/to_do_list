from django.db import models
from django.db.models import TextChoices


class Project(models.Model):
    start_date = models.DateField(
        null=False,
        blank=False,
        verbose_name='start date'
    )

    end_date = models.DateField(
        null=True,
        verbose_name='end date'
    )

    title = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    description = models.TextField(
        max_length=3000,
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'

    def __str__(self):
        return f'{self.title}'
