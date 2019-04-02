from django.db import models

class Post(models.Model):
    tag =  models.CharField(max_length = 50,null=True, blank=True)
    title = models.CharField(max_length = 100,null=True, blank=True)
    slug = models.SlugField(unique=True,max_length = 100,null=True, blank=True)
    smalldescription = models.CharField(max_length = 200,null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    image = models.TextField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True, auto_now_add=True) 

    def __str__(self):
        return self.title

