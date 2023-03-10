from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    # dunder str method return cat name
    def __str__(self):
        return self.name
    
    # this is used to direct to the detail view for a resource
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id })