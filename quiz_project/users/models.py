from django.db import models
from django.contrib.auth.models import AbstractUser
# from quiz.models import Quiz,Questions,Options

# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    uid = models.UUIDField(primary_key=True, unique=True,editable=False)
    password = models.CharField(max_length=8)
    phone_number = models.IntegerField()
    INSTRUCTOR = 'INSTRUCTOR'
    NORMAL = 'NORMAL'
    usertype_choices = ((INSTRUCTOR, 'INSTRUCTOR'), (NORMAL, 'NORMAL'))
    usertype = models.CharField(
        max_length=10, choices=usertype_choices, default=NORMAL)
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table='users'

