from tastypie.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User


class Games(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    year_released = models.IntegerField(blank=True, null=True)
    publisher = models.CharField(max_length=500, blank=True, null=True)
    genre = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'games'