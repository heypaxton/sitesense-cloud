from django.contrib import admin
from .models import *

class WorksiteAdmin(admin.ModelAdmin):
    list_display = ("site_name", "address", "city", "state", "zip_code", "created_at")
    search_fields = ["site_name", "address", "city", "state", "zip_code", "created_at"]

class DeviceAdmin(admin.ModelAdmin):
    list_display = ("worksite", "reading_url", "device_name", "created_at")
    search_fields = ["worksite", "reading_url", "device_name", "created_at"]

class ReadingAdmin(admin.ModelAdmin):
    list_display = ("device", "data", "created_at")
    search_fields = ["device", "data", "created_at"]

admin.site.register(Reading)
admin.site.register(Worksite)
admin.site.register(Device)
