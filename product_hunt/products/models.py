from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    app_name = models.CharField(default='例如:抖音-记录美好生活',max_length=100)
    introduction = models.CharField(default='在这里写app描述',max_length=256)
    link = models.CharField(default='例如:https://www.baidu.com',max_length=100)
    icon = models.ImageField(default='default_icon.jpg',upload_to='images')
    image = models.ImageField(default='default_pic.png', upload_to='images')
    votes = models.IntegerField(default=0)
    pub_date = models.DateField()
    hunter = models.ForeignKey(User,on_delete = models.CASCADE)

    def __str__(self):

        return self.app_name
