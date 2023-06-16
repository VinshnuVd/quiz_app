from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from quiz.models import Quiz

# Create your views here.
@login_required
def quiz_list(request):
    try:
        quizzes = Quiz.objects.all()
        data = Quiz()
        data.title = 'Sample Quiz'
        data.id = 1
        quizzes = [data]
        return render(request, 'quiz/quiz_list.html', {'quizzes' : quizzes})
    except Exception as e:
        print(e)

def attempt_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.question_set.all()
    return render(request, 'quiz/quiz_detail.html', {'quiz': quiz})