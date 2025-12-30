
from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin

class GenreInline(admin.TabularInline,TranslationInlineModelAdmin):
    model = Genre
    extra = 1

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    inlines = [GenreInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
class ActorImageInline(admin.TabularInline):
    model = ActorImage
    extra = 1

@admin.register(Actor)
class ActorAdmin(TranslationAdmin):
    inlines = [ActorImageInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
class MovieVideoInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = MovieVideo
    extra = 1

class MovieFrameInline(admin.TabularInline):
    model = MovieFrame
    extra = 1

@admin.register(Movie)
class MovieAdmin(TranslationAdmin):
    inlines = [MovieVideoInline, MovieFrameInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.13.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Country,Director,)
class AllAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(UserProfile)
admin.site.register(Rating)
admin.site.register(Review)
admin.site.register(ReviewLike)
admin.site.register(Favorite)
admin.site.register(FavoriteItem)
admin.site.register(History)

