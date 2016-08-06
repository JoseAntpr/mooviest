from django.db import models


GENDER_CHOICES = (
    (FEMALE, "Female"),
    (MALE, "Male")
)
# Create your models here.
class UserMovie(models.Model):
    username = models.CharField(max_length = 25)
    name = models.CharField(max_length = 30)
    lastname = models.CharField(max_lenght = 40)
    born = models.DateField(auto_now = false)
    gender = models.CharField(choices = GENDER_CHOICES)
    photo_profile = models.ImageField (upload_to = "user/profile" ,default = "user/profile/no-image.png",null=True)
    cover_page = models.ImageField (upload_to = "user/cover" ,default = "user/cover/no-image.png",null=True)
    email = models.EmailField(max_length = 254)
