from django.db import models

# Create your models here.
class Post(models.Model):


    title = models.CharField(max_length=700)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True) 
    #auto_now_add = True means that the date will be set to the current date and time when the object is created.