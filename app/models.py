from django.db import models

# Create your models here.
class UserList(models.Model):
    scr = models.CharField(default='',max_length=280,unique=True)
    name = models.CharField(default='',max_length=280)

    def __str__(self):
        return f'{self.scr}'

class Tweet(models.Model):
    tw_id = models.CharField(default='',max_length=280,unique=True)
    dt = models.DateTimeField()
    author = models.ForeignKey(UserList,on_delete=models.CASCADE, related_name='tweets',null=True)
    usr = models.CharField(default='',max_length=280)
    scr = models.CharField(default='',max_length=280)
    txt = models.CharField(default='',max_length=280)
    
    def __str__(self):
        return f'{self.usr} > {self.txt}'
