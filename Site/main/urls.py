
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('top10', views.top10),
    path('add', views.add),
]
