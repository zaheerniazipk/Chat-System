from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class friend_list(models.Model):
    from_user=models.ForeignKey(User,related_name="from_user",on_delete=models.CASCADE)
    to_user=models.ForeignKey(User,related_name="to_user",on_delete=models.CASCADE)


class msg(models.Model):
    message=models.TextField(max_length=1000)
    date=models.DateTimeField(default=datetime.now)
    sender=models.TextField(max_length=200)
    reciver=models.TextField(max_length=200)


