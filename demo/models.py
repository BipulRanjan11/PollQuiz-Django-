from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):

    mobile = models.BigIntegerField(blank = True, null= True)
    created_at=models.DateTimeField(auto_now=True)

class UserNdPassword(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=150)



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
