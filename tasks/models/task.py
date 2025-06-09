from django.db import models
from gettext import gettext as _


class TaskStatus(models.TextChoices):
    PENDING = ('P', _('pending'))
    DONE = ('D', _('done'))


class Task(models.Model):

    title = models.CharField(
        max_length=255,
        verbose_name=_('title'),
    )

    description = models.TextField(
        verbose_name=_('description'),
    )

    status = models.CharField(
        max_length=1,
        choices=TaskStatus.choices,
        default=TaskStatus.PENDING,
        blank=True,
        verbose_name=_('status')
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.status:
            self.status = TaskStatus.PENDING
        return super().save(*args, **kwargs)
