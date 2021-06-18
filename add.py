
import json
import os
import sys
from datetime import datetime, timedelta

import django
from requests_oauthlib import OAuth1Session

sys.path.append('n575')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'n575.settings')
django.setup()

if os.path.exists('local.py'):
    from local import AT, ATS, CK, CS
else:
    AT = os.environ['AT']
    ATS = os.environ['ATS']
    CK = os.environ['CK']
    CS = os.environ['CS']

twitter = OAuth1Session(CK, CS, AT, ATS)  # 認証処理

url = 'https://api.twitter.com/1.1/search/tweets.json'
from app.models import Tweet, UserList

keyword = '#n575'
params = {'count': 100, 'q': keyword}
req = twitter.get(url, params=params)

if req.status_code == 200:
    res = json.loads(req.text)
    for line in res['statuses']:
        if '#n575' in line['text']:
            if line['text'] == '#n575':
                continue
            if line['text'][:2] == 'RT':
                continue
            dt = datetime.strptime(
                line['created_at'], '%a %b %d %H:%M:%S %z %Y')
            dt = dt + timedelta(hours=9)
            tw_id = line['id_str']
            usr = line['user']['name']
            scr = line['user']['screen_name']
            txt = line['text']
            fav = line['favorite_count']
            ret = line['retweet_count']
            Tweet.objects.update_or_create(
                tw_id=tw_id,
                dt=dt,
                usr=usr,
                scr=scr,
                txt=txt,
                fav=fav,
                ret=ret,
                score=ret*10+fav,
            )
            UserList.objects.update_or_create(
                usr_id=scr,
                name=usr,
            )
else:
    print("Failed: %d" % req.status_code)
