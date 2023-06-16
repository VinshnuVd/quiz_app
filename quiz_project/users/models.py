import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    INSTRUCTOR = 'instructor'
    STUDENT = 'student'
    USERTYPE_CHOICES = [
        (INSTRUCTOR, 'Instructor'),
        (STUDENT, 'Student'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    usertype = models.CharField(max_length=10, choices=USERTYPE_CHOICES)

    class Meta:
        indexes = [
            models.Index(fields=["username"]),
        ]