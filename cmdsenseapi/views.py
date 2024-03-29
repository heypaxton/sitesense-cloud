from django.shortcuts import render, redirect
import http
import json
import dweepy

from rest_framework import viewsets

from .serializers import *
from .models import *

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_user(request):
    """
    Login user
    """
    logout_user(request)
    print("outside POST")
    # POST request
    if request.method == 'POST':
        print("inside POST")
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        print("~~user")
        print(user)

        if user and user.is_active:
            login(request, user)
            print("logged in")
            return HttpResponseRedirect('/')

    # GET request
    return render(request, 'registration/login.html')

def logout_user(request):
    """
    Logout user
    """
    logout(request)
    return HttpResponseRedirect('/')

def forget_password(request):
    """
    Logout user
    """
    if request.method == 'POST':
        return HttpResponseRedirect('/confirm_mail')
    return render(request, 'registration/forget_password.html')

def confirm_mail(request):
    """
    Logout user
    """
    return render(request, 'registration/confirm_mail.html')

@login_required
def index(request):
    return render(request, 'index.html')

def read(request):
    readings = Reading.objects.all()
    return render(request, 'readings/read.html', {'readings': readings})

def read_position(request):
    sensor = dweepy.get_latest_dweet_for('sitesense-sensor')
    sensor = sensor[0]['content']

    tag = dweepy.get_latest_dweet_for('cmdsense-tag')
    tag = tag[0]['content']

    gps = dweepy.get_latest_dweet_for('sitesense-gps')
    gps = gps[0]['content']

    Reading.objects.create(
        area_id=1,
        data={"sensor": sensor, "tag": tag, "gps": gps}
    )
    return redirect(read)

@login_required
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
