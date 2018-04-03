from django.db import models
from django.utils import timezone


# This specifies the type of data in each attribute
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # This will save the post and set the published attribute to the current date/time
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
