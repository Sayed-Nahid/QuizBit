from django.urls import path
from . import views
urlpatterns = [
    path('questions/', views.questions, name="questions"),
    path("submit_quiz/", views.submit_quiz, name="submit_quiz"),
    path('quiz_history/', views.quiz_history, name="quiz_history")
]
