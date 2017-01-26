from django.contrib.postgres.fields import JSONField
from django.utils import timezone
from django.db import models

# Create your models here.
class Reading(models.Model):
    data = JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)
