from django.shortcuts import render
from .models import Question, Student
from .serializers import QuestionSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def questions(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def submit_quiz(request):
    username = request.data.get("username")
    username = username.upper()
    score = request.data.get("score")
    student = Student.objects.get(username=username)
    student.score = score
    student.status = "done"
    student.save()
    return Response({"You Have Completed the Quiz. See you in Leaderboard."})