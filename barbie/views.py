from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def progress(request):
    return render(request, 'progress.html')

def news(request):
    return render(request, 'news.html')

def fanpage(request):
    return render(request, 'fanpage.html')

def community(request):
    return render(request, 'community.html')