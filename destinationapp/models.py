from django.db import models

# Create your models here.
class Destination(models.Model):
    PlaceName = models.CharField(max_length=255)
    Weather = models.CharField(max_length=255)
    State = models.CharField(max_length=255)
    District = models.CharField(max_length=255)
    GoogleMap = models.URLField(max_length=255)
    Description = models.CharField(max_length=5000)
    Images = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.PlaceName