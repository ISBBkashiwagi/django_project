from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional
    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username

class MicroPost(models.Model):
    content = models.TextField(max_length=140)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=timezone.now())

class IsbbEmployee(models.Model):
    name = models.TextField(max_length=140)
    age = models.IntegerField()
    join_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name
