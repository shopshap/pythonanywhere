from django.urls import path
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('',views.indexuser, name='indexuser'),
    path('admin/',admin.site.urls),
    path('', views.thaistory, name='thaistory'),
    path('', views.thaistoryuser, name='thaistoryuser'),
    path('', views.International, name='International'),
    path('', views.Internationaluser, name='Internationaluser'),
    path('', views.Login, name='Login'),
    path('', views.Register, name='Register'),
]