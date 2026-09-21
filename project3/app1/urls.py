from django.urls import path
from .import views

urlpatterns=[
    path('',views.view1,name="view1"),
    path('loans/',views.view2,name="view2")
]