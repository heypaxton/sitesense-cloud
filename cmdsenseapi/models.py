from django.contrib.postgres.fields import JSONField
from django.utils import timezone
from django.db import models


class Worksite(models.Model):
    site_name = models.CharField(max_length=100)
    descripton = models.TextField(default='')
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)
        db_table = 'worksite'

    def __str__(self):
        return self.site_name

class Device(models.Model):
    worksite = models.ForeignKey(Worksite, on_delete=models.CASCADE)
    reading_url = models.CharField(max_length=255)
    device_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)
        db_table = 'device'

    def __str__(self):
        return self.device_name

class Reading(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    data = JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)
        db_table = 'reading'
