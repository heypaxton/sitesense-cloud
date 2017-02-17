from .models import *
from rest_framework import serializers

class WorksiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Worksite
        fields = ('site_name', 'address', 'city', 'state', 'zip_code', 'created_at')

class AreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Area
        fields = ('area_name', 'worksite', 'created_at')

class ReadingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reading
        fields = ('device_id', 'data', 'created_at')
