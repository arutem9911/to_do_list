from django.db import models
from django.db import models
from django.db.models import TextChoices


class Status(models.Model):
    status = models.CharField(
        max_length=200,
        null=False,  # <null>
        blank=False,
        default='new',
        verbose_name='status'
    )

    class Meta:
        verbose_name = 'status'
        verbose_name_plural = 'statuses'

    def __str__(self):
        return f'{self.status}'
