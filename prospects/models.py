from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
     pass

class SalesRep(models.Model):
     """
     Class representing information about the Sales
     Representative.
     """

     user = models.OneToOneField(User, on_delete=models.CASCADE)
     first_name = models.CharField(max_length=20)
     last_name = models.CharField(max_length=20)
     email = models.EmailField()
     display_picture = models.ImageField(blank=True, null=True)


class Prospect(models.Model):
     """
     Class representing information about the Sales Prospects
     gotten from different sales sources.
     """

     PROSPECTIVE_SOURCES = (
          ('Call Centre', 'Call Centre'),
          ('Social Media Ads', 'Social Media Ads'),
          ('Door-to-door', 'Door-to-door'),
     )

     first_name = models.CharField(max_length=20)
     last_name = models.CharField(max_length=20)
     age = models.IntegerField(default=0)
     email = models.EmailField()
     display_picture = models.ImageField(blank=True, null=True)
     source = models.CharField(choices=PROSPECTIVE_SOURCES, max_length=100)
     agent = models.ForeignKey("Agent", on_delete=models.CASCADE)