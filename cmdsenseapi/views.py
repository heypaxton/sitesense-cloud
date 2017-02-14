from django.shortcuts import render
import http
import json

from rest_framework import viewsets

from .serializers import *
from .models import *

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login(request):
    """
    Login user
    """
    # logout(request)
    print("outside POST")
    # POST request
    if request.method == 'POST':
        print("inside POST")
        username = request.POST.get('username')
        password = request.POST.get('password')

        # user authentication for username & password
        user = authenticate(username=username, password=password)
        login(request, user)
        print(username)
        print(password)
        return HttpResponseRedirect('/')

    # GET request
    return render(request, 'registration/login.html')

def logout(request):
    """
    Logout user
    """
    logout(request)
    return HttpResponseRedirect('/')

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
