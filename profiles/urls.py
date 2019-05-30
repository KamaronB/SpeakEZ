from django.urls import path
from profiles import views

urlpatterns = [
    path('', views.pro, name='pro'),
    path(r'^results/$', views.search_user,name="search"),
    path('update/',views.update_account,name="update"),
    path('friend_request',views.friend_request,name="friend request"),
    path('requests/',views.show_requests, name="show requests"),

]
