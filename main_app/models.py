from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Q

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
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

