from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Content(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content_name = models.CharField(max_length=256)
    content_info = models.TextField(blank=True)
    content_date = models.DateField()
    content_likes = models.IntegerField()
    content_dislikes = models.IntegerField()

    def __str__(self):
        return str(self.content_name)


class Comment(models.Model):
    comment_content = models.ForeignKey(Content, on_delete=models.CASCADE)
    comment_info = models.TextField(blank=True)
    comment_date = models.DateField()
    comment_likes = models.IntegerField()
    comment_dislikes = models.IntegerField()