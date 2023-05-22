from django.shortcuts import render,HttpResponse,redirect

def index(request):
    return render(request,"index.html")

def agecal(request):
    return render(request,'agecal.html')
