from django.db import models

# Create your models here.
class  Artiste(models.Model):
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    age = models.IntegerField()
    
    
    def _str_(self):
        return self.first_name
        
        
class Song(models.Model):
    artiste = models.ForeignKey("Artiste", blank = True, null = True, on_delete = models.CASCADE)
    title = models.CharField(max_length = 400)
    date_released = models.DateTimeField(auto_now_add = True)
    likes = models.IntegerField()
    artist_id = models.CharField(max_length = 40)
    
    
    def _str_(self):
        return self.title
        
        
        
class Lyric(models.Model):
    song = models.ForeignKey("Song", blank = True, null = True, on_delete = models.CASCADE)
    content = models.CharField( max_length = 1400)
    songg_id = models.CharField(max_length=40)
    
    
    def _str_(self):
        return self.content