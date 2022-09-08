from django.shortcuts import render
from .models import Book


def index(request):
    context = {'books': Book.objects.all()}
    return render(request, 'index.html', context)

