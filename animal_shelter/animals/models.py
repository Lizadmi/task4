from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    age = models.IntegerField()
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='animals_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
