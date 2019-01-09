from django.db import models

# Create your models here.


class Participant(models.Model):
    participant_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=30,null=True)
    dob = models.DateField(null=True)
    barcode = models.IntegerField(unique=True,
        default=1234567890)
    def __str__(self):
        return self.first_name

    
class Attendance(models.Model):
    morning = 'AM'
    evening = 'PM'
    time_of_day_choices = ((morning, 'Morning'),(evening, 'Evening'))
    participant_id = models.IntegerField(unique=True)
    datetime_attendance_logged = models.DateTimeField()
    time_of_day = models.CharField(max_length=2, 
        choices=time_of_day_choices)

    