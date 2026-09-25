from . import views
from django.urls import path

urlpatterns = [
    path('', views.view1, name='playlist'),
]