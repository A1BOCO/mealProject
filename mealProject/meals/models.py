import time

from django.conf import settings
from django.core import validators
from django.db import models

# Create your models here.
MEALTIME_CHOICES = [
    (1, 'morning'),
    (2, 'afternoon'),
    (3, 'evening'),
]

class CustomDateTimeField(models.DateTimeField):
    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        if val:
            val.replace(microsecond=0)
            return val.isoformat()
        return ''


class Meal(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to='images/',blank=True)
    country_of_origin = models.CharField(max_length=30)
    typical_mealtime = models.IntegerField(choices=MEALTIME_CHOICES)
    date_added = models.DateTimeField(auto_now=True)
    number_of_votes = models.IntegerField(null=True,default=0)
    tags = models.ManyToManyField('tag')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, null=True,
    )


class MealRating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    rating = models.FloatField([validators.MinValueValidator(0.0), validators.MaxValueValidator(5.0)])
    dete_of_rating = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

