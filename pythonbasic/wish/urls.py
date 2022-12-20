from django.urls import path

from . import views

urlpatterns = [
    path('', views.firstpage),
    path('wish/', views.secondpage),
    path('wish/wish/wish/pic', views.thirdpage),
    path('wish/wish/wish/wish/wish/wish/wish/wish/wish/wish/wish/wish/wish/wish/wish/pic/gift/', views.fourthpage),
]