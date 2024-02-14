from django.urls import path
from . import views

app_name = 'museum'
urlpatterns = [
    path('', views.index, name='index'),

]