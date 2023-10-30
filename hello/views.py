from django.http import HttpResponse
from django.shortcuts import render, redirect 
from django.contrib.auth import logout 
from .models import lostdeposit

# Create your views here.
def index(request):
    return render(request, "hello/main.html")

def logout_view(request):
    return render(request)
    return redirect("/")

def data_visualization(request):
    data = lostdeposit.objects.all()
    return render(request, 'hello/visualisation.html', {'data': data})