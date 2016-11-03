from django.contrib import admin
import nested_admin
# Register your models here.
from .models import *

class Catalogue_langInline(admin.TabularInline):
    model = Catalogue_lang
    extra = 0

class CatalogueInline(nested_admin.NestedStackedInline):
    model = Catalogue
    extra = 0
    inlines = [Catalogue_langInline]

class RatingInline(admin.StackedInline):
    model = Rating
    extra = 0

class ParticipationInline(admin.StackedInline):
    model = Participation
    extra = 1

class Movie_langInline(admin.StackedInline):
    model = Movie_lang
    extra = 1


class MovieAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        Movie_langInline,
        RatingInline,
        ParticipationInline,
        CatalogueInline,
    ]

    # def get_search_results(self, request, queryset, search_term):
    #     queryset, use_distinct = super(MovieAdmin, self).get_search_results(request, queryset, search_term)
    #     movie_langs = Movie_lang.objects.filter(
    #             Q(title__icontains=search_term) | Q(movie__original_title__icontains=search_term), lang__code='es')
    #
    # # add to queryset the results of finding the Movies that matches the movie_langs ids
    #     queryset |= Movie.objects.filter()
    #     return queryset, use_distinct


class Saga_langInline(admin.StackedInline):
    model = Saga_lang
    extra = 1

class SagaAdmin(admin.ModelAdmin):
    inlines = [Saga_langInline]

class Genre_langInline(admin.StackedInline):
    model = Genre_lang
    extra = 1

class GenreAdmin(admin.ModelAdmin):
    inlines = [Genre_langInline]

class Celebrity_langInline(admin.StackedInline):
    model = Celebrity_lang
    extra = 0

class CelebrityAdmin(admin.ModelAdmin):
    inlines = [
        Celebrity_langInline,
        ParticipationInline,
    ]

class Role_langInline(admin.StackedInline):
    model = Role_lang
    extra = 0

class RoleAdmin(admin.ModelAdmin):
    inlines = [Role_langInline]

class Emotion_langInline(admin.StackedInline):
    model = Emotion_lang
    extra = 1

class EmotionAdmin(admin.ModelAdmin):
    inlines = [Emotion_langInline]


admin.site.register(Movie,MovieAdmin)
admin.site.register(Lang)
admin.site.register(Country)
admin.site.register(Celebrity,CelebrityAdmin)
admin.site.register(Role,RoleAdmin)
admin.site.register(Saga,SagaAdmin)
admin.site.register(Genre,GenreAdmin)
admin.site.register(Emotion,EmotionAdmin)
#admin.site.register(Participation)
admin.site.register(Streaming)
#admin.site.register(Catalogue,CatalogueAdmin)
#admin.site.register(Rating)
admin.site.register(Source)
