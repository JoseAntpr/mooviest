from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile,TypeMovie,Collection,Relationship,LikeCelebrity

# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(TypeMovie)
admin.site.register(Collection)
admin.site.register(LikeCelebrity)
admin.site.register(Relationship)
