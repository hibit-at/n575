import random
from collections import defaultdict

from django.http import HttpResponse  # 追加
from django.shortcuts import render

from app.models import Tweet, UserList

# Create your views here.

def index(request):#追加
    data = Tweet.objects.order_by('dt').reverse().all()
    userlist = UserList.objects.all()
    many = defaultdict(int)
    for d in data:
        many[d.scr] += 1
    many = sorted(many.items(), key=lambda x:-x[1])
    many = many[:5]
    dic_list = []
    for m in many:
        scr = m[0]
        obj = UserList.objects.get(usr_id = scr)
        name = obj.name
        dic_list.append({'scr':scr,'user':name, 'num':m[1]})
    choice = random.randint(0,5)
    top = Tweet.objects.order_by('dt').reverse()[:20].values()
    top = list(top)
    top = sorted(top,key=lambda x : -x['score'])
    print(top)
    top = top[choice]
    params = {'data': data, 'userlist' : user_list, 'many' : dic_list , 'top' : top}
    return render(request, 'index.html', params)

def user_list(request):
    data = UserList.objects.all()
    params = {'data' : data}
    return render(request, 'userlist.html',params)
