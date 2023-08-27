from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class Content(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content_name = models.CharField(max_length=256)
    content_info = models.TextField(blank=True)
    content_date = models.DateField(default=datetime.date.today)
    content_likes = models.IntegerField(default=0)
    content_dislikes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.content_name)


class Comment(models.Model):
    comment_content = models.ForeignKey(Content, on_delete=models.CASCADE)
    who_post = models.ForeignKey(User, on_delete=models.CASCADE, related_name='who_post')
    to_whom = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_whom')
    comment_info = models.TextField(blank=True)
    comment_date = models.DateField(default=datetime.date.today)