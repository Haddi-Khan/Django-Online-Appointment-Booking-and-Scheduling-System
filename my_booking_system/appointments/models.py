from django.db import models
from django.contrib.auth.models import User


class Appointment(models.Model):
    # User jo booking kar raha hai
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Kaunsi service chahiye (e.g. Doctor, Barber, Consultant)
    service = models.CharField(max_length=100)

    # Kis din aur kis time?
    date = models.DateField()
    time = models.TimeField()

    # Booking ka status
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.service} ({self.date})"
