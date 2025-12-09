from django.urls import path
from .views import user_feed
from .views import LikePostView, UnlikePostView

urlpatterns = [
    path("feed/", user_feed, name="user_feed"),
    path("<int:pk>/like/", LikePostView.as_view(), name="like_post"),
    path("<int:pk>/unlike/", UnlikePostView.as_view(), name="unlike_post"),
]