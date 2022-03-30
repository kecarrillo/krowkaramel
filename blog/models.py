from django.conf import settings
from django.db import models
from django.utils import timezone

class CategoryPost(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='medias/')
    text = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    category_blog = models.ForeignKey(CategoryPost, on_delete=models.CASCADE, default="none")

    def __str__(self):
        return self.title
