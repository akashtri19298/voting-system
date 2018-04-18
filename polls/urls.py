from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #path('', RedirectView.as_view(url='/polls/')),
    path('',views.index,name="index"),
    path('index/',views.index,name="index"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('results/',views.results,name="results"),
    path('vote/',views.vote,name="vote"),
    
]

