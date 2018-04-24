from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('', RedirectView.as_view(url='/polls/')),
    path('',views.index,name="index"),
    path('index/',views.index,name="index"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('results/',views.results,name="results"),
    path('vote/',views.vote,name="vote"),
    path('reg_successful',views.reg_successful,name="reg_successful"),
    path('invalid_vote',views.invalid_vote,name="invalid_vote"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)