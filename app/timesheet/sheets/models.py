from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        """Returns string representation of project name."""
        return self.name


class Activity(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'activities'

    def __str__(self):
        """Returns string representation of activity"""
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        """Returns string representation of a client"""
        return self.name


class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=30)
    mail = models.EmailField(max_length=100)

    def __str__(self):
        """Returns string representation of a user"""
        return self.username


class Timesheet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    monday = models.PositiveSmallIntegerField()
    tuesday = models.PositiveSmallIntegerField()
    wednesday = models.PositiveSmallIntegerField()
    thursday = models.PositiveSmallIntegerField()
    friday = models.PositiveSmallIntegerField()
    saturday = models.PositiveSmallIntegerField()
    sunday = models.PositiveSmallIntegerField()
