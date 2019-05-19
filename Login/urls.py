from django.urls import path
from Login import views

urlpatterns = [
    path('', views.main, name='main'),
    path('register',views.register,name='register'),
    path('about', views.about, name='about'),
    path('logout', views.logout_view, name='logout'),

]
