from django.db import models
from users.models import Trainer

class FitnessProgram(models.Model):
    DAYS_OF_WEEK = (
        ('MONDAY', 'Monday'),
        ('TUESDAY', 'Tuesday'),
        ('WEDNESDAY', 'Wednesday'),
        ('THURSDAY', 'Thursday'),
        ('FRIDAY', 'Friday'),
        ('SATURDAY', 'Saturday'),
        ('SUNDAY', 'Sunday'),
    )
    TIME = (
        ('08:00 - 09:00', '8:00 am - 9:00 am'),
        ('09:00 - 10:00', '9:00 am - 10:00 am'),
        ('10:00 - 11:00', '10:00 am - 11:00 am'),
        ('18:00 - 19:00', '6:00 pm - 7:00 pm'),
        ('19:00 - 20:00', '7:00 pm - 8:00 pm'),
        ('20:00 - 21:00', '8:00 pm - 9:00 pm'),
    )
    program_id = models.AutoField(primary_key=True)
    program_name = models.CharField(max_length=100)
    program_day = models.CharField(max_length=20, choices=DAYS_OF_WEEK)
    program_time = models.CharField(max_length=50, choices=TIME)
    program_pax = models.IntegerField()
    program_price = models.DecimalField(max_digits=10, decimal_places=2)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    program_images = models.ImageField(upload_to='program_images/', null=True, blank=True)
