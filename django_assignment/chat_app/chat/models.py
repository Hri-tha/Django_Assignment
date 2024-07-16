# chat/models.py
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=100)
    prompt = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
