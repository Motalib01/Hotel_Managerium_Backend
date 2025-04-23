from django.db import models

class Room(models.Model):
    ROOM_TYPE = (
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
    )
    room_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10, choices=ROOM_TYPE)
    features = models.TextField()
    discount_used = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Room {self.room_number} ({self.type})"
