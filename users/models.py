from django.db import models
from django.contrib.auth.models import User
from movie.models import Lang, Country, Movie, Emotion

FEMALE = "FE"
MALE = "MA"

GENDER_CHOICES = (
    (FEMALE, "Female"),
    (MALE, "Male")
)

RELATIONSHIP_FOLLOWING = 1
RELATIONSHIP_BLOCKED = 2

RELATIONSHIP_STATUSES = ((RELATIONSHIP_FOLLOWING, 'Following'), (RELATIONSHIP_BLOCKED, 'Blocked'))

class TypeMovie (models.Model):
    name = models.CharField(max_length = 15)
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    born = models.DateField()
    gender = models.CharField(max_length=6 ,choices = GENDER_CHOICES)
    photo_profile = models.ImageField (upload_to = "user/profile",default = "user/profile/no-image.png",null = True)
    cover_page = models.ImageField (upload_to = "user/cover",default = "user/cover/no-image.png",null = True)
    city = models.CharField(max_length = 35)
    country = models.ForeignKey(Country, on_delete = models.CASCADE)
    lang = models.ForeignKey(Lang, on_delete = models.CASCADE)
    collections = models.ManyToManyField(Movie, through = 'Collection')
    feelings = models.ManyToManyField(Emotion, through = 'Feeling')
    relationships = models.ManyToManyField("self", through = 'Relationship', symmetrical = False, related_name='related_to')

class Relationship (models.Model):
    from_person = models.ForeignKey(Profile, related_name='from_people')
    to_person = models.ForeignKey(Profile, related_name='to_people')
    status = models.IntegerField(choices=RELATIONSHIP_STATUSES)

class Collection (models.Model):
    user = models.ForeignKey(Profile, on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    typeMovie = models.ForeignKey(TypeMovie, on_delete = models.CASCADE)
    pub_date = models.DateTimeField(auto_now = True, null= True)
    class Meta:
        unique_together = (("movie", "user"),)

class Feeling (models.Model):
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    emotion = models.ForeignKey(Emotion, on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add = True, null= True)
