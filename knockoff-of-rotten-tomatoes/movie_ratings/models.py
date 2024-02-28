from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='movie_images/', null=True, blank=True)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()
    director = models.CharField(max_length=255)
    cast = models.TextField()
    duration = models.PositiveIntegerField()
    language = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()

    def __str__(self):
        return f"{self.user} - {self.movie}"
    
    class Meta:
        unique_together = (('user', 'movie'),)