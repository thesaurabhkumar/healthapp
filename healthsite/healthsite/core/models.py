from __future__ import unicode_literals
from django.db import models
from datetime import datetime



class ExerciseData(models.Model):
    Exercise_name = models.CharField(max_length=100, default='none')
    Exercise_muscles = models.CharField(max_length=500, default='none')
    Exercise_taker_level = models.CharField(max_length=100, default='none')
    Exercise_sets = models.CharField(max_length=30, default='none')
    Exercise_reps = models.CharField(max_length=30, default='none')
    Exercise_description = models.CharField(max_length=5000, default='none')
    Exercise_adder = models.CharField(max_length=500, default='none')
    Exercise_addition_date = models.DateTimeField(default=datetime.now, blank=True)


class TraineeTrainerData(models.Model):
    Trainee_name = models.CharField(max_length=30, default='none')
    Trainer_name = models.CharField(max_length=30, default='none')

