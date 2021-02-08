from accounts.views import ProfileRetrieveUpdateView, UserListView
from django.urls import path

app_name = "accounts"
urlpatterns = [
    path("", UserListView.as_view(), name="user-list"),
    path("profile/", ProfileRetrieveUpdateView.as_view(), name="profile-update/"),
]
