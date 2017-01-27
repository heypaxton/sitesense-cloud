from django.contrib.postgres.fields import JSONField
from django.utils import timezone
from django.db import models


class Worksite(models.Model):
    site_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=20)
    zip_code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)

class Device(models.Model):
    worksite = models.ForeignKey(Worksite)
    reading_url = models.CharField(max_length=100)
    device_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)

class Reading(models.Model):
    device = models.ForeignKey(Device)
    data = JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)
