from django.db import models

# Create your models here.

class Note(models.Model):
    title= models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    created_at = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self) -> str:
        return "Title: " + self.title + " Description: " + self.description