from django.db import models


class Todo(models.Model):
    subject = models.TextField(max_length=250)
    body = models.TextField()
    date = models.TimeField(auto_now='true')
