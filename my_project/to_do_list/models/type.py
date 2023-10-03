from django.db import models
from django.db import models
from django.db.models import TextChoices


class Type(models.Model):
    type = models.CharField(
        max_length=200,
        null=False,  # <null>
        blank=False,
        default='Task',
        verbose_name='Type'
    )

    class Meta:
        verbose_name = 'type'
        verbose_name_plural = 'types'

    def __str__(self):
        return f'{self.type}'
