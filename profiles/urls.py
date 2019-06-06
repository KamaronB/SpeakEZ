from django.urls import path
from django import urls
from profiles import views
app_name = 'profiles'

urlpatterns = [
    path('', views.pro, name='pro'),
    path(r'^results/$', views.search_user,name="search"),
    path('update/',views.update_account,name="update"),
    path('friend_request',views.friend_request,name="friend request"),
    path('requests/',views.show_requests, name="show requests"),
    path('requests/accepted',views.accept_request,name="accept"),
    path('chat',views.show_friends,name="chat"),
    path('/room',views.create_chat_room,name="new_room"),
    path('chat/room/<uuid:room_name>',views.chat_room,name='chat_room'),

]
