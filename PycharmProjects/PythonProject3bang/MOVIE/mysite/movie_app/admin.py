from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin

class GenreInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = Genre
    extra = 1

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Country, Director, Actor, Movie, MovieVideo)
class ProductAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass
@admin.register(MovieFrame)
class MovieVideoAdmin(admin.ModelAdmin):
    pass
@admin.register(Rating)
class GenreAdmin(admin.ModelAdmin):
    pass
@admin.register(Review)
class GenreAdmin(admin.ModelAdmin):
    pass
@admin.register(Favorite)
class GenreAdmin(admin.ModelAdmin):
    pass
@admin.register(FavoriteItem)
class GenreAdmin(admin.ModelAdmin):
    pass
@admin.register(History)
class GenreAdmin(admin.ModelAdmin):
    pass