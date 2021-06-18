from django.db import models

# Create your models here.

class Tweet(models.Model):
    tw_id = models.CharField(default='',max_length=280,unique=True)
    dt = models.DateTimeField()
    usr = models.CharField(default='',max_length=280)
    scr = models.CharField(default='',max_length=280)
    txt = models.CharField(default='',max_length=280)
    fav = models.IntegerField(default=0)
    ret = models.IntegerField(default=0)
    score = models.IntegerField(default=0)

class UserList(models.Model):
    usr_id = models.CharField(default='',max_length=280,unique=True)
    name = models.CharField(default='',max_length=280)
