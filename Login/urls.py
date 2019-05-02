from django.urls import path
from Login import views

urlpatterns = [
    path('', views.Login, name='Login'),
]
