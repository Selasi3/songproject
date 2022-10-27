from django.db import models

# Create your models here.
class Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=18)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Song(models.Model):
    title = models.CharField(max_length=50)
    date_released = models.DateField()
    likes = models.IntegerField()
    artist = models.ForeignKey("Artist",  on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Lyric(models.Model):
    content = models.CharField(max_length=500)
    song = models.ForeignKey("Song", on_delete=models.CASCADE)

    def __str__(self):
        return self.song.title
    