from django.urls import path, include
from .views import helloAPI, randomQuiz

urlpatterns = [
    path('helloworld/', helloAPI),
    path('<int:id>/', randomQuiz),
]
