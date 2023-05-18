from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('html/login.html',views.login_view,name='login_view'),
    path('html/signup.html',views.signup,name='signup'),
    path('html/home.html',views.home,name='home'),


]