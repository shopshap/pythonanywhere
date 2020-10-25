from django.urls import path
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('indexuser',views.indexuser, name='indexuser'),
    path('admin/',admin.site.urls),
    path('requeststory', views.requeststory, name='requeststory'),
    path('thaistory', views.thaistory, name='thaistory'),
    path('thaistoryuser', views.thaistoryuser, name='thaistoryuser'),
    path('International', views.International, name='International'),
    path('Internationaluser', views.Internationaluser, name='Internationaluser'),
    path('Login', views.Login, name='Login'),
    path('Register', views.Register, name='Register'),
]