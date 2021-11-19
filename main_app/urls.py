from django.urls import path
from . import views
from .views import MemberView

urlpatterns = [
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('', views.GroupList.as_view(), name="home"),
    path('group/new', views.GroupCreate.as_view(), name="group_create"),
    path('profile', views.Profile.as_view(), name="profile"),
    path('group/<int:pk>/update', views.GroupUpdate.as_view(), name="group_update"),
    path('group/<int:pk>/delete', views.GroupDelete.as_view(), name="group_delete"),
    path('member/<int:pk>', MemberView, name="member_group"),
    # path('golf-groups/', views.GroupList.as_view(), name="groups"),
]