from django.urls import path

from . import views

urlpatterns = [
    path('', views.firstpage),
    path('wish/', views.secondpage),
    path('wish/pic/', views.thirdpage),
    path('wish/pic/wish/pic/gift/', views.fourthpage),
]