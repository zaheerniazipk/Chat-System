from django.urls import path
from . import views

# namespace
app_name = 'chat'

# url patterns path
urlpatterns = [
    path('', views.index,  name='index'),
    path('register', views.register,  name='register'),
    path('login', views.login,  name='login'),
    path('chat', views.chat,  name='chat'),
]
