from modeltranslation.translator import TranslationOptions, register
from .models import Category, Genre, Director, Actor, Country, Movie, MovieVideo,Review




@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('genre_name',)


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)


@register(Director)
class DirectorTranslationOptions(TranslationOptions):
    fields = ('full_name', 'bio')


@register(Actor)
class ActorTranslationOptions(TranslationOptions):
    fields = ('full_name', 'bio')


@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('movie_name', 'movie_type', 'movie_status')


@register(MovieVideo)
class MovieVideoTranslationOptions(TranslationOptions):
    fields = ('video_name',)

@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('comment',)

