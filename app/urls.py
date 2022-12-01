from django.urls import path,include
from .views import UserRegistraion,UserLogin,UserProfileView

urlpatterns = [
    path('register/',UserRegistraion.as_view(),name="user registration"),
    path('login/',UserLogin.as_view(),name="user login"),
    path('profile/',UserProfileView.as_view(),name="user profile")


]
