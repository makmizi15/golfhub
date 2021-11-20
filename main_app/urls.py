from django.urls import path
from . import views
from .views import MemberView

urlpatterns = [
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('', views.GroupList.as_view(), name="home"),
    path('group/new', views.GroupCreate.as_view(), name="group_create"),
    path('group/<int:pk>/update', views.GroupUpdate.as_view(), name="group_update"),
    path('group/<int:pk>/delete', views.GroupDelete.as_view(), name="group_delete"),
    path('profile/<int:pk>', views.ProfileView.as_view(), name="profile"),
    path('profile/new', views.ProfileCreate.as_view(), name="profile_create"),
    path('profile/<int:pk>/update', views.ProfileUpdate.as_view(), name="profile_update"),
    path('member/<int:pk>', MemberView, name="member_group"),
    # path('golf-groups/', views.GroupList.as_view(), name="groups"),
]