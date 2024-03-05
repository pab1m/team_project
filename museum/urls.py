from django.urls import path
from . import views

app_name = 'museum'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.login, name='login'),
    path('password_forgotten/', views.password_forgotten, name='password_forgotten'),

]
