from django.db import models

# Create your models here.
class GalleryImage(models.Model):
    image= models.ImageField(upload_to="media")
    blur= models.ImageField(upload_to='media')
