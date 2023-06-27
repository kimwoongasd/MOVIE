from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from .models import *
from .serializers import *

# Create your views here.
class MovieList(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActorList(ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    
    
class MovieDetail(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ActorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    
class ReviewList(ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        movie = get_object_or_404(Movie, pk=self.kwargs.get('pk'))
        return Review.objects.filter(movie=movie)

    def perform_create(self, serializer):
        movie = get_object_or_404(Movie, pk=self.kwargs.get('pk'))
        serializer.save(movie=movie)
        
