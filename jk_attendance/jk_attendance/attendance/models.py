from django.db import models
import datetime as datetime


# Create your models here.


class Participant(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=30,null=True)
    dob = models.DateField(null=True)
    barcode = models.IntegerField(unique=True,
        default=1234567890)
    points = models.IntegerField(null=True)

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.points)

    
class Attendance(models.Model):
    MORNING = 'AM'
    EVENING = 'PM'
    time_of_day_choices = ((MORNING, 'Morning'),(EVENING, 'Evening'))

    participant = models.ForeignKey(Participant,on_delete=models.CASCADE)
    datetime_attendance_logged = models.DateTimeField()
    date = models.DateField(auto_now_add=True)
    time_of_day = models.CharField(max_length=2, 
                                   choices=time_of_day_choices)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.participant.first_name + ' ' + self.time_of_day + ' ' + str(self.points)

    class Meta:
        unique_together = (('participant', 'date', 'time_of_day'),)

    