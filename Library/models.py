from django.db import models

# Create your models here.

class Library(models.Model):
    Id = models.AutoField(primary_key=True)
    book_Name = models.CharField(max_length=100)
    Quantity = models.IntegerField()
    book_genre = models.CharField(max_length=20)
    Is_best_seller = models.CharField(max_length=3)
    Created_at = models.DateField()
    Updated_at = models.DateField()