from django.urls import path
from . import views

# namespace
app_name = 'chat'

# url patterns path
urlpatterns = [
    path('', views.index,  name='index'),
]
