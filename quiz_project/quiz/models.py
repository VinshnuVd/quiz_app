from django.db import models

from users.models import User

# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=25)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'quiz'


class Question(models.Model):
    text = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    class Meta:
        db_table = 'question'


class Option(models.Model):
    text = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField()

    class Meta:
        db_table = 'option'


class StudentQuizAttempt(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    submitted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'student_quiz_attempt'


class StudentQuizResponses(models.Model):
    attempt = models.ForeignKey(StudentQuizAttempt, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, on_delete=models.CASCADE)

    class Meta:
        db_table = 'student_quiz_repsonses'