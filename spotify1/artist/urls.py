from . import views
from django.urls import path

urlpatterns = [
    path('', views.view1, name='artist'),
    path('', views.home, name='home'),
]