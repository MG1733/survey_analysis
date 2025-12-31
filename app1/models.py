from django.db import models

# Create your models here.
# SURVEY FORM 
class Survey_form(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    Native = models.CharField(max_length=50)
    degree = models.CharField(max_length=100)
    sleep_hours = models.CharField(max_length=50)
    social_media_hours = models.CharField(max_length=50)
    social_media = models.CharField(max_length=50)
    eat_on_time = models.CharField(max_length=50)
    physical_activity = models.CharField(max_length=50)
    how_productive = models.CharField(max_length=100)
    experiencing_stress = models.CharField(max_length=50)
    loneliness = models.CharField(max_length=50)
    overthinking = models.CharField(max_length=100)
    self_proudness = models.CharField(max_length=50)
    learn_new = models.CharField(max_length=50)
    want_in_life = models.CharField(max_length=100)
    felt_no_potential = models.CharField(max_length=100)
    employement_status = models.CharField(max_length=50)
    career_pressure = models.CharField(max_length=100)
    financial_stability = models.CharField(max_length=50)
    money_management = models.CharField(max_length=100)
    mental_health_financially = models.CharField(max_length=50)
    self_dependencies = models.CharField(max_length=100)
    reflect_for_past = models.CharField(max_length=100)

    submitted_at = models.DateTimeField(auto_now_add=True)  # optional, to track submission time

    def __str__(self):
        return f"{self.name} -{self.age} yrs"