from django.db import models
from django.conf import settings


# Create your models here.
class Vote(models.Model):
    title = models.CharField(max_length=200)
    issue_r = models.CharField(max_length=500)
    issue_b = models.CharField(max_length=500)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='votes')


class Comment(models.Model):
    RED = 'red'
    BLUE = 'blue'
    PICK_CHOICES = (
        (RED, 'red'),
        (BLUE, 'blue')
    )
    pick = models.CharField(max_length=4, choices=PICK_CHOICES, default=RED)
    content = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE, related_name='comments')
