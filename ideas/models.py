from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Ideas_Group(models.Model):
    category_text = models.CharField(max_length=30, unique=True)
    # votes = models.IntegerField(default=0)

    def __str__(self):
        return self.category_text

class Idea(models.Model):
    idea_title = models.CharField(max_length=30)
    idea_text = models.CharField(max_length=200)
    idea_repo = models.URLField(max_length=80, blank=True, null=True)
    idea_owner = models.CharField(max_length=30, blank=True, null=True)
    idea_status = models.CharField(max_length=30, blank=True, null=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    group = models.ForeignKey(Ideas_Group, on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s by %s => %s" % (self.idea_title, self.idea_owner, self.idea_text)

    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)
    
