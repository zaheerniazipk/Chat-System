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
]
