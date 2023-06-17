from django.db import models
from users.models import User

# Create your models here.
class Options(models.Model):
    option=models.CharField(max_length=200)

    class Meta:
        db_table='options'


class Questions(models.Model):
    question=models.TextField()
    options=models.ManyToManyField(Options)
    answer=models.ForeignKey(Options,on_delete=models.DO_NOTHING,related_name='correct_answer')

    def __str__(self) -> str:
        return self.question
    
    class Meta:
        db_table='questions'


class Quiz(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    instructor=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    question=models.ManyToManyField(Questions)
    is_active=models.BooleanField(default=False)
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table='quiz'



class UserAttempts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='attempted_user')
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name='user_attempted_quiz')
    user_attempts=models.IntegerField(default=0)

    class Meta:
        unique_together=('user','quiz')
        db_table='userattempts'

# class UserResponses(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='rensponse_provided_by')
#     question=models.ForeignKey(Questions,on_delete=models.CASCADE,related_name='user_attempted_question')
#     selected_option=models.ForeignKey(Options,on_delete=models.DO_NOTHING)

#     class Meta:
#         db_table='useresponses'