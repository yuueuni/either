from django.db import models


# Create your models here.
class Vote(models.Model):
    title = models.CharField(max_length=200)
    issue_a = models.CharField(max_length=500)
    issue_b = models.CharField(max_length=500)


class Comment(models.Model):
    AGREE = 'AG'
    DISAGREE = 'DAG'
    PICK_CHOICES = (
        (AGREE, 'Agree'),
        (DISAGREE, 'Disagree')
    )
    pick = models.CharField(max_length=2, choices=PICK_CHOICES, default=AGREE)
    content = models.CharField(max_length=200)
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE, related_name='comments')
