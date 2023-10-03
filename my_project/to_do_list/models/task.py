from django.db import models
from django.db import models
from django.db.models import TextChoices


class Tasks(models.Model):
    short_description = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    description = models.TextField(
        max_length=3000,
        null=False,
        blank=True
    )

    status = models.ForeignKey(
        'to_do_list.Status',
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='status',
        default=1
    )

    type = models.ForeignKey(
        'to_do_list.Type',
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='type',
        default=1
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='created at'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='updated at'
    )

    project = models.ForeignKey(
        'to_do_list.Project',
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='project',
        default=1
    )

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'

    def __str__(self):
        return f'{self.short_description} | {self.status} | {self.type}'
