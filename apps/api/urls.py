from django.urls import path
from .views import ChuckNorrisView

urlpatterns = [
    path('chucknorris/', ChuckNorrisView.as_view()),
]