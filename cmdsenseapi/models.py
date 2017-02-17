from django.contrib.postgres.fields import JSONField
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


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

class Area(models.Model):
    worksite = models.ForeignKey(Worksite, on_delete=models.CASCADE)
    area_name = models.CharField(max_length=100)
    description = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)
        db_table = 'area'

    def __str__(self):
        return self.area_name


class Reading(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE, default=1)
    data = JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)
        db_table = 'reading'
