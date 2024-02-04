from django.db import models
from users.models import Trainer

class FitnessProgram(models.Model):
    program_id = models.AutoField(primary_key=True)
    program_name = models.CharField(max_length=100)
    program_day = models.CharField(max_length=50)
    program_time = models.CharField(max_length=50)
    program_pax = models.IntegerField()
    program_price = models.DecimalField(max_digits=10, decimal_places=2)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    program_images = models.ImageField(upload_to='program_images/', null=True, blank=True)