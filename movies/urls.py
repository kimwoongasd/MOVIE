from django.urls import path
from .views import MovieList, movie_detail, ActorList, actor_detail, review_list

urlpatterns = [
    path('movies', MovieList.as_view()),
    path('actors', ActorList.as_view()),
]