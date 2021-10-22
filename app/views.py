import random
from collections import defaultdict
from math import ceil

from django.http import HttpResponse  # 追加
from django.shortcuts import render

from app.models import Tweet, UserList

# Create your views here.


def index(request):  # 追加
    page = 1
    if 'page' in request.GET:
        page = int(request.GET['page'])
    span = 50
    start = (page-1)*span
    end = start+span
    all_data = Tweet.objects.order_by('dt').reverse()
    all_tweet = len(Tweet.objects.all())
    all_pages = ceil(all_tweet/span)
    data = all_data[start:end]
    many = defaultdict(int)
    for a in all_data:
        many[a.scr] += 1
    many = sorted(many.items(), key=lambda x: -x[1])
    many = many[:7]
    dic_list = []
    for m in many:
        scr = m[0]
        obj = UserList.objects.get(usr_id=scr)
        name = obj.name
        dic_list.append({'scr': scr, 'user': name, 'num': m[1]})
    choice = random.randint(0, 5)
    top = Tweet.objects.order_by('dt').reverse()[:30].values()
    top = list(top)
    top = sorted(top, key=lambda x: -x['score'])
    top = top[choice]
    end = min(end,all_tweet)
    params = {'data': data, 'userlist': user_list,
              'many': dic_list, 'top': top, 'len' : all_tweet,
              'page' : page, 'all_pages' : all_pages,
              'start' : start, 'end' : end,}
    return render(request, 'index.html', params)


def ini(request, word=''):
    if 'word' in request.POST:
        word = request.POST['word']
    data = Tweet.objects.filter(txt__contains=word).order_by('dt')
    if len(data) > 0:
        first = data[0]
    else:
        first = None
    if word == '':
        first  = None
    data = Tweet.objects.filter(txt__contains=word).order_by('dt').reverse()
    params = {'first': first, 'data': data, 'word': word}
    return render(request, 'ini.html', params)


def user_list(request):
    data = UserList.objects.all()
    params = {'data': data}
    return render(request, 'userlist.html', params)


def person(request):

    user = request.GET.get('user')
    data = Tweet.objects.filter(scr=user).order_by('dt').reverse()
    top = data[0]
    path = request.get_full_path()
    obj = UserList.objects.get(usr_id=user)
    name = obj.name
    params = {'data': data, 'top': top, 'name': name}
    return render(request, 'person.html', params)
