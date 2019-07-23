from django.db import models

# classCreate your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    opening_time = models.DateTimeField()
    closing_time = models.DateTimeField()
    def __str__(self):
        return self.name
