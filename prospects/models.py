from django.db import models


class Prospect(models.Model):
     first_name = models.CharField(max_length=20)
     last_name = models.CharField(max_length=20)
     age = models.IntegerField(default=0)
     email = models.EmailField()
