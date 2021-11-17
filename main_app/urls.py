from django.urls import path
from . import views

urlpatterns = [
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('', views.GroupList.as_view(), name="home"),
    path('group/new', views.GroupCreate.as_view(), name="group_create"),
    path('profile/', views.Profile.as_view(), name="profile"),
    # path('golf-groups/', views.GroupList.as_view(), name="groups"),
]