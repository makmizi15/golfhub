from django.urls import path
from . import views

urlpatterns = [
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('', views.Home.as_view(), name="home")
]