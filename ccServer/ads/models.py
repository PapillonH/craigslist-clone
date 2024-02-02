from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Ad(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)


# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Ad

get.post.update.delete