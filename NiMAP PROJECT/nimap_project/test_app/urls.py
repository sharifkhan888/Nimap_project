from django.contrib import admin
from django.urls import path
from .import views as v
urlpatterns = [
    path('user', v.ListCreateUser.as_view()),
    path('ruduser/<int:pk>', v.RUDUser.as_view()),
    path('client', v.ListCreateClient.as_view()),
    path('rudclient/<int:pk>', v.RUDClient.as_view()),
    path('project', v.ListCreateProject.as_view()),
    path('rudproject/<int:pk>', v.RUDProject.as_view()),
]

