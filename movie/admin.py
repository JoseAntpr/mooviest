from django.contrib import admin

# Register your models here.
from .models import Lang, Country, Movie, Celebrity, Celebrity_lang,Role,Role_lang,Saga,Saga_lang,Genre,Genre_lang,Emotion,Emotion_lang,Movie,Movie_lang,Participation,Streaming,Catalogue,Catalogue_lang,Rating,Source



admin.site.register(Lang)
admin.site.register(Country)
admin.site.register(Celebrity)
admin.site.register(Celebrity_lang)
admin.site.register(Role)
admin.site.register(Role_lang)
admin.site.register(Saga)
admin.site.register(Saga_lang)
admin.site.register(Genre)
admin.site.register(Genre_lang)
admin.site.register(Emotion)
admin.site.register(Emotion_lang)
admin.site.register(Movie)
admin.site.register(Movie_lang)
admin.site.register(Participation)
admin.site.register(Streaming)
admin.site.register(Catalogue)
admin.site.register(Catalogue_lang)
admin.site.register(Rating)
admin.site.register(Source)
