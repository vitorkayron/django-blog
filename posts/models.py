from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateField(auto_created=True)
    images =  models.ImageField()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title