from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),               
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
 
]
