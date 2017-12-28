from django.db import models
from django.utils.timezone import now

# Create your models here.


# Define documents
class EventregistryPost(models.Model):
    news_id = models.IntegerField(primary_key=True)
    source_id = models.IntegerField()
    source_url = models.CharField(max_length=250)
    source_title = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    body = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    image = models.ImageField(upload_to="static/img/", null=True, blank=True)
    created_at = models.DateTimeField(max_length=150, default=now().strftime('%Y-%m-%d %H:%M:%S'))
    tags = models.CharField(max_length=250, default="Fake News")

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return format(self.title)