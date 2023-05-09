from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    weather = models.CharField(max_length=50)
    mood = models.CharField(max_length=50)
    body = models.TextField()
    image = models.ImageField(upload_to="blog/", blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:20]