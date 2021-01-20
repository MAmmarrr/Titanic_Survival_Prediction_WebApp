from django.urls import path
from . import views

urlpatterns = [
    path('', views.SurvivalLaujk, name='getScore'),
    path('score', views.score, name="getScore")
]