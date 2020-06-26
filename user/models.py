from django.db import models
import datetime
from django.utils import timezone
import pytz
from timezone_field import TimeZoneField

class User(models.Model):

    id          = models.AutoField(primary_key=True)
    real_name   = models.CharField(max_length=40)
    tz          = TimeZoneField(default='UTC', choices=[(tz, tz) for tz in pytz.all_timezones])

    def __str__(self):
        return self.real_name

class ActivityPeriod(models.Model):
    id          = models.AutoField(primary_key=True)
    start_time  = models.DateTimeField()
    end_time    = models.DateTimeField()
    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['start_time']