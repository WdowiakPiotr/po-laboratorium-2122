from django.db import models
import datetime
from datetime import timezone


class Question (models.Model):
    question = models.TextField(max_length=100)
    pub_date = models.DateTimeField('Publication date')

    def __str__(self):
        return self.question
        
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice (models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=20)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text