from . import views
from django.urls import path

urlpatterns = [
    path('', views.view1, name='view1'),
    path('', views.home, name='home'),
    
    
]