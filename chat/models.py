from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class message(models.Model):
    # complain_id=models.ForeignKey(complain,on_delete=models.CASCADE)
    message=models.TextField(max_length=1000)
    # we have set this field for admin and customer we will use true for customer and false for admin
    reply=models.BooleanField()
    date=models.DateTimeField(default=datetime.now)