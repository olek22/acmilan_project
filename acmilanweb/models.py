from django.db import models


class Club(models.Model):
     name = models.CharField(max_length=64, blank=False, unique=True)
     year = models.PositiveSmallIntegerField(null=True, blank=True)
     stadium = models.CharField(max_length=64, blank=False)
     stadium_capacity = models.PositiveIntegerField(null=True, blank=True)
     colors = models.CharField(max_length=64, blank=True, null=True)
     nickname = models.CharField(max_length=64, blank=True, null=True)
     web_site = models.URLField(max_length=200, blank=True)
     description = models.TextField(default="")
     club_crest = models.ImageField(upload_to="club_crest", blank=True)

     def __str__(self):
          return self.name

     @property
     def stadium_with_capacity(self):
          return f"{self.stadium} ({self.stadium_capacity})"




