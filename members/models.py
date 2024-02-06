from django.db import models
from trainers.models import FitnessProgram
from users.models import Member
from webpages.models import Plan

# Create your models here.
class ProgramEnroll(models.Model):
    id = models.AutoField(primary_key=True)
    program = models.ForeignKey(FitnessProgram, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return f"Enrollment #{self.id} - Program: {self.program}, Member: {self.member}"


class PlanSubscribe(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return f"Enrollment #{self.id} - Plan: {self.plan}, Member: {self.member}"