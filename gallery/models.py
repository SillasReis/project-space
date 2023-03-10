from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):

    CATEGORIES = [
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALÁXIA', 'Galáxia'),
        ('PLANETA', 'Planeta'),
    ]

    name = models.CharField(max_length=100, null=False, blank=False)
    subtitle = models.CharField(max_length=150, null=False, blank=False)
    category = models.CharField(max_length=100, choices=CATEGORIES, default='')
    description = models.TextField(null=False, blank=False)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)
    
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=False, related_name='user')

    def __str__(self):
        return self.name
