from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from movie.models import Lang, Country, Movie,Movie_lang, Emotion, Celebrity
from imagekit.models import ProcessedImageField,ImageSpecField
from imagekit.processors import ResizeToFill,SmartResize

FEMALE = "FE"
MALE = "MA"

GENDER_CHOICES = (
    (FEMALE, "Female"),
    (MALE, "Male")
)

RELATIONSHIP_FOLLOWING = 1
RELATIONSHIP_BLOCKED = 2

RELATIONSHIP_STATUSES = ((RELATIONSHIP_FOLLOWING, 'Following'), (RELATIONSHIP_BLOCKED, 'Blocked'))

def user_directory_path_profile(instance,filename):
    return 'user/user_{0}/profile/{1}'.format(instance.user.id,filename)

class TypeMovie (models.Model):
    name = models.CharField(max_length = 15)
    def __str__(self):              # __unicode__ on Python 2
        return self.name
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,primary_key = True ,on_delete=models.CASCADE)
    born = models.DateField(null = True, blank = True)
    gender = models.CharField(max_length=6 ,choices = GENDER_CHOICES,blank = True,null = True)
    avatar = ProcessedImageField (upload_to = user_directory_path_profile,default = "user/default/no-image.png",
    processors=[ResizeToFill(180,180)],format='JPEG',options={'quality':60} ,null = True, blank = True)
    avatar_thumbnail = ImageSpecField(source='avatar',processors=[SmartResize(30,30)],format='JPEG',options={'quality':60})
    cover_page = models.ImageField (upload_to = user_directory_path_profile,default = "user/default/no-image.png",null = True, blank = True)
    city = models.CharField(max_length = 35, blank = True, null = True)
    postalCode = models.CharField(max_length = 35, null = True, blank = True)
    country = models.ForeignKey(Country,null = True, blank = True)
    lang = models.ForeignKey(Lang,null = True, blank= True)
    collections = models.ManyToManyField(Movie, through = 'Collection', blank = True)
    feelings = models.ManyToManyField(Emotion, through = 'Feeling', blank = True)
    relationships = models.ManyToManyField("self", through = 'Relationship', symmetrical = False, related_name='related_to', blank = True)
    likeCelebrities = models.ManyToManyField(Celebrity, through = 'LikeCelebrity', blank = True)

    def __str__(self):              # __unicode__ on Python 2
        return self.user.username

    def get_relationships(self,status):
        return self.relationships.filter(
            to_people__status=status,
            to_people__from_person=self)

    def get_related_to(self,status):
        return self.related_to.filter(
            from_people__status=status,
            from_people__to_person=self)

    def get_following(self):
        return self.get_relationships(RELATIONSHIP_FOLLOWING)

    def get_followers(self):
        return self.get_related_to(RELATIONSHIP_FOLLOWING)
    def get_seenlist(self):
        return Movie_lang.objects.filter(lang__code = 'es').select_related('movie').filter(movie__collection__user=self, movie__collection__typeMovie__name='seen')
    def get_watchlist(self):
        return Movie_lang.objects.filter(lang__code = 'es').select_related('movie').filter(movie__collection__user=self, movie__collection__typeMovie__name='watchlist')
    def get_favouritelist(self):
        return Movie_lang.objects.filter(lang__code = 'es').select_related('movie').filter(movie__collection__user=self, movie__collection__typeMovie__name='favourite')
    def get_likecelebrities(self):
        return self.likeCelebrities.all()
    def get_typemovie(self, movie):
        try:
            typeMovie = Collection.objects.get(user = self, movie = movie).typeMovie
        except ObjectDoesNotExist:
            typeMovie = None
        return typeMovie

class Relationship (models.Model):
    from_person = models.ForeignKey(Profile, related_name='from_people')
    to_person = models.ForeignKey(Profile, related_name='to_people')
    status = models.IntegerField(choices=RELATIONSHIP_STATUSES)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.from_person.user.username) + " sigue a " + str(self.to_person.user.username)

    class Meta:
        unique_together = (("from_person", "to_person"),)

class Collection (models.Model):
    user = models.ForeignKey(Profile, on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE, related_name='collection')
    typeMovie = models.ForeignKey(TypeMovie, on_delete = models.CASCADE)
    pub_date = models.DateTimeField(auto_now = True, null= True)
    class Meta:
        unique_together = (("movie", "user"),)
    #def __str__(self):
        #return self.movie

class Feeling (models.Model):
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    emotion = models.ForeignKey(Emotion, on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add = True, null= True)

class LikeCelebrity (models.Model):
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    celebrity = models.ForeignKey(Celebrity, on_delete = models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add = True, null= True)
