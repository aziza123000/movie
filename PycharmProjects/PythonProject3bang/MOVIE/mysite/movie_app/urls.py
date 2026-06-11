from rest_framework import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (UserProfileViewSet, CategoryListAPIView, CategoryDetailAPIView, GenreListAPIView, GenreDetailAPIView, CountryViewSet, DirectorViewSet, ActorViewSet, MovieLisrAPIView, MovieDetailAPIView, MovieVideoViewSet, MovieFrameViewSet, RatingViewSet, ReviewViewSet, FavoriteViewSet, FavoriteItemViewSet, HistoryItemViewSet)

router = DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'directors', DirectorViewSet)
router.register(r'actors', ActorViewSet)
router.register(r'movie_video', MovieVideoViewSet)
router.register(r'movie_frame', MovieFrameViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'favorites', FavoriteViewSet)
router.register(r'favorite_items', FavoriteItemViewSet)
router.register(r'history', HistoryItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('genre/', GenreListAPIView.as_view(), name='genre_list'),
    path('genre/<int:pk>/', GenreDetailAPIView.as_view(), name='genre_detail'),
    path('movie/', MovieLisrAPIView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailAPIView.as_view(), name='movie_detail'),
]