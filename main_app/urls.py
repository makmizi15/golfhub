from django.urls import path
from . import views

urlpatterns = [
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('', views.Home.as_view(), name="home"),
    path('profile/', views.Profile.as_view(), name="profile"),
    path('golf-groups/', views.Groups.as_view(), name="groups"),
]