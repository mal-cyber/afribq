from django.db import models

# Create your models here.
class gallery(models.Model):
    Img = models.ImageField(upload_to='gallery/%d/')
