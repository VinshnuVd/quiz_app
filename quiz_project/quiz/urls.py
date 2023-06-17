from django.urls import path
from quiz.views import QuizList,QuestionAPI

urlpatterns=[
    path('quiz/',QuizList.as_view(),name='quiz-list'),
    path('questions/',QuestionAPI.as_view(),name='questions')
]