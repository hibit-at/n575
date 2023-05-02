from rest_framework import serializers
from .models import Tweet,UserList

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'

class UserListSerializer(serializers.ModelSerializer):
    tweets_size = serializers.IntegerField()

    class Meta:
        model = UserList
        fields = ('scr', 'name', 'tweets_size')