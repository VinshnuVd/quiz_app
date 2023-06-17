from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Quiz,Questions,Options,UserAttempts
from quiz_project.authentication import QuizAuthentication
from django.db import transaction


# Create your views here.


class QuizList(APIView):
    authentication_classes=[QuizAuthentication]
    # permission_classes=[]
    fields=['title','description','instructor']

    def get(self,request):
        try:
            final_data=Quiz.objects.filter(instructor_id=request.user.uid).values()
            return Response({
                'status':200,
                'data':final_data
            },status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'status':500,'data':'Internal server occured'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self,request):
        try:
            if request.user.usertype=='INSTRUCTOR':
                payload={
                            'title':request.data.get('title'),
                            'description':request.data.get('description'),
                            'instructor_id':request.user.uid
                        }
                
                Quiz.objects.create(**payload)

                return Response({
                    'status':200,
                    'data':'Success fully added quiz..'
                },status=status.HTTP_200_OK)
            else:
                return Response({"msg":"Invalid action","status":400},status=status.HTTP_400_BAD_REQUEST)

            
        except Exception as e:
            print(e)
            return Response({'status':500,'data':'Internal server occured'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self,request,pk):
        try:
            quiz_q=Quiz.objects.filter(id=pk,instructor=request.user.uid)
            if quiz_q.exists():
                quiz_obj=quiz_q.first()
                quiz_q.update(is_active=not(quiz_obj.is_active))
            else:
                return Response({"msg":"Invalid action","status":400},status=status.HTTP_400_BAD_REQUEST)
            return Response({
                'status':200,
                'data':'Success fully updated quiz status..'
            },status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'status':500,'data':'Internal server occured'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class QuestionAPI(APIView):
    authentication_classes=[QuizAuthentication]

    def get(self,request):
        try:
            quiz_id=request.data.get('quiz_id')
            quiz_q=Quiz.objects.filter(id=quiz_id)
            if quiz_q.exists():
                quiz_b=quiz_q.first()
                quiz_ques=quiz_b.question.all()
                final_data=[]
                
                for que in quiz_ques:
                    options=list(que.options.all().values())
                    if request.user.usertype=='INSTRUCTOR':
                        final_data.append({
                            'id':que.id,
                            'question':que.question,
                            'options':options,
                            'answer':que.answer.id
                        })
                    else:
                        final_data.append({
                            'id':que.id,
                            'question':que.question,
                            'options':options,
                        })



                print(final_data)
                return Response({
                        'status':200,
                        'data':final_data
                    },status=status.HTTP_200_OK)

            else:
                return Response({"msg":"Invalid action","status":400},status=status.HTTP_400_BAD_REQUEST)





            
        
        except Exception as e:
            print(e)
            return Response({'status':500,'data':'Internal server occured'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
    def post(self,request):
        try:
            if request.user.usertype=='INSTRUCTOR':
                quiz_id=request.data.get('quiz_id')
                quiz_q=Quiz.objects.filter(id=quiz_id)
                if quiz_q.exists():
                    quiz_b=quiz_q.first()
                    with transaction.atomic():
                        for q_a in request.data.get('data'):
                            option1=Options.objects.create(option=q_a.get('option1'))
                            option2=Options.objects.create(option=q_a.get('option2'))
                            option3=Options.objects.create(option=q_a.get('option3'))
                            option4=Options.objects.create(option=q_a.get('option4'))
                            index=request.data.get('answer')
                            if index==1:
                                answer=option1
                            elif index==2:
                                answer=option2
                            elif index==3:
                                answer=option3
                            else:
                                answer=option4
                            que_b=Questions.objects.create(question=q_a.get('question'),answer=answer)
                            quiz_b.question.add(que_b)
                            que_b.options.add(option1)
                            que_b.options.add(option2)
                            que_b.options.add(option3)
                            que_b.options.add(option4)
                else:
                    return Response({"msg":"Invalid action","status":400},status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"msg":"Invalid action","status":400},status=status.HTTP_400_BAD_REQUEST)

            return Response({
                    'status':200,
                    'data':'Success fully added questions..'
                },status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'status':500,'data':'Internal server occured'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserResponse(APIView):
    authentication_classes=[QuizAuthentication]

    def post(self,request):
        try:
            correct_cnt=0
            attempts=0
            total=len(request.data.get("data"))
            print(request.user.usertype)
            if request.user.usertype=='NORMAL':
                print('rfg')
                quiz_id=request.data.get("quiz_id")
                quiz_q=Quiz.objects.filter(id=quiz_id)
                print(quiz_q)
                if quiz_q.exists():
                    print(11)
                    attmt_que= UserAttempts.objects.filter(user_id=request.user.uid,quiz_id=quiz_id)
                    if attmt_que.exists():
                        print(12)

                        atmt_obj=attmt_que.first()
                        atmt_obj.user_attempts+=1
                        atmt_obj.save()
                    else:
                        print(3311)

                        atmt_obj=UserAttempts.objects.create(user_id=request.user.uid,quiz_id=quiz_id,user_attempts=1)

                    for q_a in request.data.get("data"):
                       print(67678)
                       que= Questions.objects.get(id=q_a["q_id"])
                       if que.answer_id == q_a["op_id"]:
                           correct_cnt+=1
                    final_data={
                        'no_of_attempts':atmt_obj.user_attempts,
                        'correct_responses':correct_cnt,
                        'wrong_responses':total-correct_cnt
                    }

            
                    return Response({"data":final_data,"status":200},status=status.HTTP_200_OK)
                
            print('kjbnj')
            return Response({"msg":"Invalid action","status":400},status=status.HTTP_400_BAD_REQUEST)



                    

                       

        except Exception as e:
            print(e)
            return Response({'status':500,'data':'Internal server occured'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

