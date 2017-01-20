from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Message(models.Model):
    sender = models.ForeignKey(User,related_name='sender')
    receiver = models.ForeignKey(User,related_name='receiver')
    body = models.TextField(max_length=500)
    seen = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)