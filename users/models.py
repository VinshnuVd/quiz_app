from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    uid = models.UUIDField(primary_key=True, editable=False)
    password = models.CharField(max_length=8)
    phone_number = models.IntegerField(max_length=12)
    INSTRUCTOR = 'INSTRUCTOR'
    NORMAL = 'NORMAL'
    usertype_choices = ((INSTRUCTOR, 'INSTRUCTOR'), (NORMAL, 'NORMAL'))
    usertype = models.CharField(
        max_length=10, choices=usertype_choices, default=NORMAL)
    is_active = models.BooleanField(default=False)

class UserAttempts(models.Model):
    user=models.ForeignKey(User)
    quiz=models.ForeignKey()
    user_attempts=models.IntegerField(default=0)

    class Meta:
        unique_together=('user','quiz')

class UserResponses(models.Model):
    user=models.ForeignKey(User)
    question=models.ForeignKey()
    selected_option=models.ForeignKey()