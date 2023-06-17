from django.urls import path
from quiz.views import QuizList,QuestionAPI,UserResponse

urlpatterns=[
    path('quiz/',QuizList.as_view(),name='quiz-list'),
    path('questions/',QuestionAPI.as_view(),name='questions'),
    path('response/',UserResponse.as_view(),name='UserResponse'),


]