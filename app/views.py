from django.shortcuts import render
from django.db.models import Count
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Tweet, UserList
from .serializers import TweetSerializer, UserListSerializer
from .filters import TweetFilter


class TweetListAPI(generics.ListAPIView):
    queryset = Tweet.objects.order_by('-dt')
    serializer_class = TweetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TweetFilter

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        total_results = queryset.count()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            paginated_response = self.get_paginated_response(serializer.data)
            paginated_response.data['total_results'] = total_results
            return paginated_response

        serializer = self.get_serializer(queryset, many=True)
        return Response({'results': serializer.data, 'total_results': total_results})


class UserListAPI(generics.ListAPIView):
    serializer_class = UserListSerializer

    def get_queryset(self):
        queryset = UserList.objects.annotate(
            tweets_size=Count('tweets')).order_by('-tweets_size')
        return queryset


class LuckyTweetAPI(APIView):
    def get(self, request):
        lucky_tweet = Tweet.objects.order_by('?').first()
        serializer = TweetSerializer(lucky_tweet)
        return Response(serializer.data)


def index(request):
    return render(request, 'index.html')
