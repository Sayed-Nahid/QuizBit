from django.shortcuts import render
from .models import Question, Student
from .serializers import QuestionSerializer, StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def questions(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def submit_quiz(request):
    username = request.data.get("username")
    username = username.upper()
    score = request.data.get("score")
    student = Student.objects.get(username=username)
    student.score = score
    student.status = "done"
    student.save()
    return Response({"You Have Completed the Quiz. See you in Leaderboard."})

@api_view(['GET'])
def quiz_history(request):
    history = Student.objects.all()
    serializer = StudentSerializer(history, many=True)
    return Response(serializer.data)