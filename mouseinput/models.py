from django.db import models

class MouseEvent(models.Model):
    TYPE_CHOICES = [
        ('click', 'Click'),
        ('move', 'Move'),
    ]
    event_type = models.CharField(max_length=5, choices=TYPE_CHOICES)
    x = models.IntegerField()
    y = models.IntegerField()
    timestamp = models.DateTimeField()