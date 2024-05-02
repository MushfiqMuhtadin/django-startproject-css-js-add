from django.shortcuts import render

def home(request):
    return render (request,'home.html')

def reading(request):
    return render(request,'reading.html')