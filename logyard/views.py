from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'index.html')


def display_logs(request):
    items = Logs.objects.all()
    context = {
        'items': items,
        'header': "Logs",
    }

    return render(request, 'index.html', context)


def display_plywood(request):
    items = Plywood.objects.all()
    context = {
        'items': items,
        'header': "Plywood",
    }

    return render(request, 'index.html', context)
