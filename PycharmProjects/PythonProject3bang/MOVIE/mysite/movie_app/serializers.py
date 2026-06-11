from rest_framework import serializers
from .models import (UserProfile, Category, Genre, Country, Director, Actor, Movie,  MovieVideo, MovieFrame, Rating, Review, Favorite, FavoriteItem, History)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = 'all'

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']

class GenreNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_name']


class CategoryDetailSerializer(serializers.ModelSerializer):
    genres = GenreNameSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['category_name', 'genres']

class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'genre_name']


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ['country_name']

class MovieListSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format=['%Y'])
    country = CountrySerializer(many=True)
    genre = GenreNameSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'movie_poster', 'movie_name', 'year', 'country', 'genre']

class GenreDetailSerializer(serializers.ModelSerializer):
    movie_list = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = ['genre_name']


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'all'

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = 'all'


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'all'

class MovieVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieVideo
        fields = 'all'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = 'all'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'all'

class MovieFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieFrame
        fields = 'all'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = 'all'

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = 'all'

class FavoriteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = 'all'