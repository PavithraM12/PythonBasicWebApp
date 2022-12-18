from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse


def firstpage(request):
    return render(request, "firstpage.html")

def secondpage(request):
    return render(request, "secondpage.html")

def thirdpage(request):
    return render(request, "thirdpage.html")

def fourthpage(request):
    return render(request, "fourthpage.html")
