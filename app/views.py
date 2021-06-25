import random
from collections import defaultdict

from django.http import HttpResponse  # 追加
from django.shortcuts import render

from app.models import Tweet, UserList

# Create your views here.


def index(request):  # 追加
    data = Tweet.objects.order_by('dt').reverse().all()
    userlist = UserList.objects.all()
    many = defaultdict(int)
    for d in data:
        many[d.scr] += 1
    many = sorted(many.items(), key=lambda x: -x[1])
    many = many[:5]
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
    params = {'data': data, 'userlist': user_list,
              'many': dic_list, 'top': top, 'len' : len(data)}
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
