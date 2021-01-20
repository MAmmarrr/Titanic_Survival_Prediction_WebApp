from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('SurvivalLaujk', views.SurvivalLaujk, name="getScore"),
    path('score', views.score, name="getScore")
]