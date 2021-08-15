from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=60)
    rating = models.IntegerField(
        validators=[MinValueValidator(0),MaxValueValidator(10)])
    game_designer = models.CharField(null=True , max_length=100)
    top_seller = models.BooleanField(default=False)
    slug =models.SlugField(default="", null=False,db_index=True)

    def get_absolute_url(self):
        return reverse("gamer", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    

    def __str__(self):
        return f"{self.title} ({self.rating})"
