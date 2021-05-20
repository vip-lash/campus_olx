from django.db import models
from datetime import datetime


class Team(models.Model):
  name = models.CharField(max_length=200)
  photo = models.ImageField(upload_to='photos/team/%Y/%m/%d/', blank=True)
  description = models.TextField(blank=True)
  phone = models.CharField(max_length=20, blank=True)
  email = models.CharField(max_length=50, blank=True)
  join_date = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
    return self.name
