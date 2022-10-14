from django.db import models
from django.core import validators
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100,validators=[validators.MinLengthValidator(3)])
    age = models.IntegerField(validators=[validators.MinValueValidator(10)])
    mark1 = models.IntegerField(validators=[validators.MinValueValidator(0),validators.MaxValueValidator(100)])
    mark2 = models.IntegerField(validators=[validators.MinValueValidator(0),validators.MaxValueValidator(100)])
    mark3 = models.IntegerField(validators=[validators.MinValueValidator(0),validators.MaxValueValidator(100)])
    total = models.IntegerField(validators=[validators.MinValueValidator(0),validators.MaxValueValidator(100)])
    avg = models.FloatField(validators=[validators.MinValueValidator(0),validators.MaxValueValidator(100)])
    grade = models.CharField(max_length=10)
    def __str__(self):
        return self.name