from django.db import models

# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=250)
    weather = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=250)
    google_map_link = models.URLField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.name}'
    
    
class Image(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.destination.name}'
    
    