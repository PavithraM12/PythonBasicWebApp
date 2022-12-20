from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
# from django.http import HttpResponse


def firstpage(request):
    return render(request, "firstpage.html")
@csrf_exempt
def secondpage(request):
    return render(request, "secondpage.html")
# @csrf_exempt
# def thirdpage(request):
#     import turtle
#     t = turtle.Turtle()
#     turtle.title("Hapiness")
#     t.right(100)
#     return t
@csrf_exempt
def thirdpage(request):
    return render(request, "thirdpage.html")

@csrf_exempt     
def fourthpage(request):
    return render(request, "fourthpage.html")
