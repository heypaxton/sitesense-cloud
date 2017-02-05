from django.shortcuts import render
import http
import json

from rest_framework import viewsets

from .serializers import *
from .models import *


# Create your views here.
class ReadingViewSet(viewsets.ModelViewSet):
    # Add a reading
    # current_reading = http.client.HTTPConnection("10.0.0.91:5000")
    # current_reading.request("GET", '/api/v1.0/sensor')
    # response = current_reading.getresponse()
    # sensor_data = json.dumps(response.read())
    #
    # Reading.objects.create(data=sensor_data)


    # Return reading
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer
    pass
