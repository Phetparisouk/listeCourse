
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('delete/<liste_id>', views.delete, name="delete"),
    path('barrer/<liste_id>', views.barrer, name="barrer"),
    path('debarrer/<liste_id>', views.debarrer, name="debarrer"),
    path('edit/<liste_id>', views.edit, name="edit"),
]
