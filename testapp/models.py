from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=200)
    tags = models.ManyToManyField("Tag")

class Tag(models.Model):
    name = models.CharField(max_length=200)
