from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING


class Listing(models.Model):
    user=models.ForeignKey(User,on_delete=DO_NOTHING,null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', null=True, default=0)
    photo_2 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', null=True, default=0)
    photo_3 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', null=True, default=0)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now)
    phone = models.CharField(max_length=12,default='')
    seller = models.CharField(max_length=200, default='')

def __str__(self):
    return self.title
    
