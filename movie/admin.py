from django.contrib import admin

# Register your models here.
from .models import Movie,Participation,Celebrity,Genre

class ParticipationInline(admin.TabularInline):
    model = Participation
    extra = 1
class MovieAdmin(admin.ModelAdmin):
    inlines = (ParticipationInline,)


admin.site.register(Movie,MovieAdmin)
admin.site.register(Celebrity)
admin.site.register(Genre)
