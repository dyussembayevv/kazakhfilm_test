from django.db import models


class Film(models.Model):
    name = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    synopsis = models.TextField()
    poster = models.ImageField(upload_to='posters/')
    video_link = models.URLField(max_length=200, blank=True, null=True)  # Add this field

    def __str__(self):
        return self.name


class BackstagePhoto(models.Model):
    film = models.ForeignKey(Film, related_name='backstage_photos', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='backstages/')

    def __str__(self):
        return f"Backstage photo for {self.film.name}"