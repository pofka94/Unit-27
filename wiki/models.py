from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=30, unique=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title