from django.conf import settings
from django.db import models
from django.core import validators


class MealRecommend(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to='images/',blank=True)
    country_of_origin = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now=True)
    number_of_votes = models.IntegerField(null=True,default=0)
    tags = models.ManyToManyField('MealRecommendTag')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, null=True,
    )


class MealRecommendRating(models.Model):
    meal = models.ForeignKey(MealRecommend, on_delete=models.CASCADE)
    rating = models.FloatField([validators.MinValueValidator(0.0), validators.MaxValueValidator(5.0)])
    dete_of_rating = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )

class MealRecommendTag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name