from django.shortcuts import render
import secrets
from .models import Application
from rest_framework import viewsets
from.serializers import ApplicationSerialzer
# Create your views here.

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = queryset = Application.objects.all()
    serializer_class = ApplicationSerialzer


def home(request):
    queryset = Application.objects.all()

    context = {
        "object_list": queryset,
    }
    return render(request, "home.html", context)

def new_key(request):
    key = secrets.token_urlsafe(6)
    new_app = Application(name=request.POST.get('name'), key=key)
    new_app.save()

    return home(request)


def delete_app(request):
    id = list(request.POST.keys())[1]
    app = Application.objects.filter(id=id)
    app.delete()
    return home(request)


def edit_app(request):
    id = list(request.POST.values())[1]
    obj = Application.objects.filter(id=id)
    obj.update(name=list(request.POST.keys())[1])
    return home(request)

def test_app(request):
    return home(request)