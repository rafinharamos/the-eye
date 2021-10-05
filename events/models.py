import uuid

from django.db import models
from jsonfield import JSONField


class Session(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField('created at', auto_now_add=True)


class Event(models.Model):
    session = models.ForeignKey(
        'events.Session',
        verbose_name='session',
        related_name='events',
        on_delete=models.CASCADE
    )
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    data = JSONField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.name


class EventError(models.Model):
    data = JSONField()
    message = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.message}'

    class Meta:
        verbose_name = 'Event Error'
        verbose_name_plural = 'Events Error'
