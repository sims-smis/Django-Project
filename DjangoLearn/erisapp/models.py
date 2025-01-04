from django.db import models
from django.utils import timezone

# Create your models here.
class chaiVariety(models.Model):
    CHAI_TYPE_CHOICES = [
        ('BL', 'Black Tea'),
        ('GR', 'Green Tea'),
        ('HR', 'Herbal Tea'),
        ('MS', 'Masala Tea'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/', default='adam-thomas-Ta1viaIDvIk-unsplash_JQsFeLm.jpg')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES)
    description = models.TextField(default='')
    def __str__(self):
        return self.name