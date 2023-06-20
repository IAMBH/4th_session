from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name=models.CharField(max_length=30, null=False, blank=False)

    def __str__(self) -> str:
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    # writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    weather = models.CharField(max_length=50)
    mood = models.CharField(max_length=50)
    body = models.TextField()
    image = models.ImageField(upload_to="blog/", blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    like = models.ManyToManyField(User, related_name='likes', blank=True)
    like_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:20]
    
class Comment(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField()
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='comments', blank=True)

    def __str__(self):
        return self.post.title
