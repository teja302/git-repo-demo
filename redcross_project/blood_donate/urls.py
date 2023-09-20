from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=  [
    path('', views.administrate, name='administrate'),
    path('base1/',views.base1,name="base1"),
    path('login/', views.admin_login, name='login'),
    path('logout/', views.logout_admin, name='logout'),
    


]
