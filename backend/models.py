from django.db import models

# Create your models here.


class YoutubeAPIResults(models.Model):
    videoID = models.CharField(null=False, max_length=40, blank=False)
    videoTitle = models.CharField(null=True, max_length=400)
    videoDescription = models.CharField(null=True, blank=True, max_length=4000)
    publishedAt = models.DateTimeField()
    thumbnailURL = models.URLField()
    thumbnailHeight = models.IntegerField()
    thumbnailWidth = models.IntegerField()
    channelTitle = models.CharField(max_length=400)
