from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=100)
    like_count = models.IntegerField()
    view_count = models.IntegerField()
    contents = models.TextField()

    def __str__(self):
        return self.title