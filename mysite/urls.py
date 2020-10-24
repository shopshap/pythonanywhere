from django.contrib import admin
from django.urls import path, include
from myweb import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myweb/', include('myweb.urls', namespace="myweb")),
    path('thaistory', views.thaistory),
    path('thaistoryuser', views.thaistoryuser),
    path('International', views.International),
    path('Internationaluser', views.Internationaluser),
    path('Login', views.Login),
    path('Logout', views.logout),
    path('indexuser', views.indexuser),
    path('Register', views.Register),
]
