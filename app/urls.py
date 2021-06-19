from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('user',views.user_list, name='user_list'),
    path('person/',views.person, name='person'),
]
