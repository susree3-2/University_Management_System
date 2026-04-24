from django.db import models

#Course model 
class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.IntegerField()

    def __str__(self):
        return self.name

#Room model
class Room(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name
    
# TimeSlot model (represents day + time)
class TimeSlot(models.Model):
    day = models.CharField(max_length=20)  # e.g., Monday
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.day} ({self.start_time} - {self.end_time})"


# Schedule model (connects Course + Room + Time)
class Schedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    timeslot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course} - {self.room} - {self.timeslot}"