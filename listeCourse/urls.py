
from django.contrib import admin
from django.urls import path, include
from liste import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('liste.urls')),
]
