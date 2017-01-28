from .models import *
from rest_framework import serializers

class WorksiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Worksite
        fields = ('site_name', 'address', 'city', 'state', 'zip_code', 'created_at')

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ('worksite_id', 'reading_url', 'device_name', 'created_at')

class ReadingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reading
        fields = ('device_id', 'data', 'created_at')
