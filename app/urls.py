from django.urls import path

from . import views
from .views import LuckyTweetAPI

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/tweets/', views.TweetListAPI.as_view(), name='tweet-list-api'),
    path('api/users/', views.UserListAPI.as_view(), name='user_list_api'),
    path('api/lucky_tweet/', LuckyTweetAPI.as_view(), name='lucky_tweet_api'),
]
