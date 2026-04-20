from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.IntegerField()

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name