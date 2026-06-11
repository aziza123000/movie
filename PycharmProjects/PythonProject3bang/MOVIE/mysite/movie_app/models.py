from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from  django.core.validators import MaxValueValidator,MinValueValidator

StatusChoices = (
    ('pro', 'pro'),
    ('simple', 'simple'),
)



class UserProfile(AbstractUser):
     phone_number = PhoneNumberField(null=True,blank=True)
     age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18),
                                                        MaxValueValidator(70)],
                                            null=True,blank=True)
     user_photo = models.ImageField(upload_to='user_images',null=True,blank=True)

     status = models.CharField(max_length=20,choices=StatusChoices,default='simple')
     date_register = models.DateField(auto_now_add=True,)

     def __getstate__(self):
         return f'{self.first_name},{self.last_name}'

class Category(models.Model):
    category_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
         return self.category_name

class Genre(models.Model):
    genre_name = models.CharField(max_length=30)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
         return f'{self.genre_name},{self.category}'


class Country (models.Model):
    country_name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.country_name

class Director(models.Model):
   full_name = models.CharField(max_length=100,verbose_name='ФИО')
   director_photo = models.ImageField(upload_to='director_images')
   birth_date = models.DateField()
   bio = models.TextField()

   def __str__(self):
       return self.full_name

class Actor(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    actor_photo = models.ImageField(upload_to='actor_images')
    birth_date = models.DateField()
    bio = models.TextField()

    def __str__(self):
        return self.full_name

class Movie(models.Model):
    movie_name = models.CharField(max_length=50)
    year = models.DateField()
    county = models.ManyToManyField(Country)
    director = models.ManyToManyField(Director)
    genre = models.ManyToManyField(Genre)
    MovieTypeChoices=(
        ('360p', '360p'),
        ('480p', '480p'),
        ('720p', '720p'),
        ('1080p', '1080p'),
    )
    movie_type = models.CharField(max_length=20,choices=MovieTypeChoices)
    movie_time =  models.PositiveSmallIntegerField()
    actor = models.ManyToManyField(Actor)
    movie_poster = models.ImageField(upload_to= 'movie_images')
    trailer = models.URLField()
    descriptions = models.TextField()
    movie_status = models.CharField(max_length=20,choices=StatusChoices)

    def __str__(self):
        return self.movie_name

class MovieVideo(models.Model):
    video_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    video = models.FileField(upload_to='movie_videos')
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.movie},{self.video_name}'


class MovieFrame(models.Model):
    image = models.ImageField(upload_to='movie_image')
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.movie},{self.image}'


class Rating(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField(choices=[(i ,str(i))for i in range(1,11)])
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user},{self.movie},{self.stars}'

class Review(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user},{self.comment}'

class Favorite(models.Model):
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class  FavoriteItem(models.Model):
    favorite = models.ForeignKey(Favorite,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.movie}'

class History(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user},{self.movie},{self.created_date}'




































