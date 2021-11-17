from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone, dateformat
import datetime
from django.db.models import Q
from django import forms

# format timezone.now
formatted_date = dateformat.format(timezone.localtime(), 'm/d/Y P')

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=1000)
    bio = models.TextField(max_length=500)
    location = models.CharField(max_length=100)
    handicap = models.IntegerField(validators=[MinValueValidator(0.0), MaxValueValidator(54.0)], blank=True)
    favorite_course = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        constraints = [
            # for checking that handicap is between 0 and 54 in DB
            models.CheckConstraint(
                name='profile_handicap_range',
                check=Q(handicap__gte=0.0) & Q(handicap__lte=54.0))
        ]


class GolfGroup(models.Model):  
    
    GAME_CHOICES = (
        ('2-Man Scramble', '2-Man Scramble'),
        ('Freeplay', 'Freeplay'),
    )

    creator = models.ForeignKey(Profile, on_delete=models.CASCADE, serialize=True, related_name='creator', null=True)
    golf_course = models.CharField(max_length=100)
    tee_date = models.DateField()
    tee_time = models.TimeField()
    description = models.CharField(max_length=200, help_text="Write a description in 200 words or less")
    game_type = models.CharField(max_length=50, choices=GAME_CHOICES, default="f")

    # def __str__(self):
    #     return self.golf_course
        
    # class Meta:
    #     ordering = ['tee_time']

# class MyModel(models.Model):
#     my_date = models.DateField('my date')



