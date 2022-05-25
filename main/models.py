from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=100)
    like_count = models.IntegerField()
    view_count = models.IntegerField()
    contents = models.TextField()

    def __str__(self):
        return f'제목:{self.title}, 좋아요 수:{self.like_count}, 조회수:{self.view_count}'