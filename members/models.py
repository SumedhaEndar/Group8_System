from django.db import models
from trainers.models import FitnessProgram
from users.models import Member
from webpages.models import Plan
from django.utils import timezone
from datetime import timedelta
# Create your models here.
class ProgramEnroll(models.Model):
    id = models.AutoField(primary_key=True)
    program = models.ForeignKey(FitnessProgram, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    left = models.IntegerField(default=13)

    def __str__(self):
        return f"Enrollment #{self.id} - Program: {self.program}, Member: {self.member}"


class PlanSubscribe(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    valid_from = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField(default=timezone.now() + timedelta(days=30))

    def __str__(self):
        return f"Enrollment #{self.id} - Plan: {self.plan}, Member: {self.member}"