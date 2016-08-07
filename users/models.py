from django.db import models
from django.contrib.auth.models import User
from movie.models import Lang,Country,Movie

FEMALE = "FE"
MALE = "MA"

GENDER_CHOICES = (
    (FEMALE, "Female"),
    (MALE, "Male")
)

class TypeMovie (models.Model):
    name = models.CharField(max_length = 15)
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    born = models.DateField()
    gender = models.CharField(max_length=6 ,choices = GENDER_CHOICES)
    photo_profile = models.ImageField (upload_to = "user/profile" ,default = "user/profile/no-image.png",null = True)
    cover_page = models.ImageField (upload_to = "user/cover" ,default = "user/cover/no-image.png",null = True)
    city = models.CharField(max_length = 35)
    country = models.ForeignKey(Country, on_delete = models.CASCADE)
    lang = models.ForeignKey(Lang, on_delete = models.CASCADE)
    followers = models.ManyToManyField("self", symmetrical = False)
    movies = models.ManyToManyField(Movie, through = 'Collection')

class Collection (models.Model):
    user = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    typeMovie = models.ForeignKey(TypeMovie, on_delete = models.CASCADE)
    class Meta:
        unique_together = (("movie", "user"),)
