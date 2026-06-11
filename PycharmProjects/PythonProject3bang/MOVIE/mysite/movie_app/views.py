from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.serializers import ListSerializer

from .models import (UserProfile, Category, Genre, Country, Director, Actor, Movie, MovieVideo, MovieFrame, Rating, Review, Favorite, FavoriteItem, History)
from.serializers import (UserProfileSerializer, CategoryListSerializer, CategoryDetailSerializer, GenreListSerializer, GenreDetailtSerializer, CountrySerializer, DirectorSerializer, ActorSerializer, MovieListSerializer, MovieDetailSerializer, MovieVideoSerializer, MovieFrameSerializer, RatingSerializer, ReviewSerializer, FavoriteSerializer, FavoriteItemSerializer, HistorySerializer)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer

class GenreListAPIView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreListSerializer

class GenreDetailAPIView(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreDetailtSerializer

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class MovieLisrAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer

class MovieDetailAPIView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer

class MovieVideoViewSet(viewsets.ModelViewSet):
    queryset = MovieVideo.objects.all()
    serializer_class = MovieVideoSerializer

class MovieFrameViewSet(viewsets.ModelViewSet):
    queryset = MovieFrame.objects.all()
    serializer_class = MovieFrameSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class FavoriteItemViewSet(viewsets.ModelViewSet):
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteItemSerializer

class HistoryItemViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer