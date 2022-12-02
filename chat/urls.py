from django.urls import path
from . import views

# namespace
app_name = 'chat'

# url patterns path
urlpatterns = [
    # path('', views.index,  name='index'),
    path('register', views.register_user,  name='register'),
    path('', views.login_user,  name='login_user'),
    path('chat', views.chat,  name='chat_app'),
    path('chat-group', views.chat_group,  name='chat_group'),
    path('logout', views.user_logout,  name='Logout'),
    path('send_id', views.send_id,  name='send_id'),
]
