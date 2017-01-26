from .models import Reading
from rest_framework import serializers

class ReadingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reading
        fields = ('data', 'created_at')
