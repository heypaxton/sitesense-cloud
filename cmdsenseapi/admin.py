from __future__ import unicode_literals

from django.contrib import admin
from .models import *

class WorksiteAdmin(admin.ModelAdmin):
    list_display = ("site_name", "address", "city", "state", "zip_code", "created_at")
    search_fields = ["site_name", "address", "city", "state", "zip_code", "created_at"]

class AreaAdmin(admin.ModelAdmin):
    list_display = ("worksite", "area_name")
    search_fields = ["worksite", "area_name"]
#
class ReadingAdmin(admin.ModelAdmin):
    list_display = ("area", "data", "created_at")
    search_fields = ["area", "data", "created_at"]

admin.site.register(Worksite, WorksiteAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Reading, ReadingAdmin)
