from django.db import models

# Create your models here.

class DailyTasks(models.Model):
    user_name=models.CharField(max_length=50)
    daily_tasks=models.CharField(max_length=120)
    completion = models.BooleanField(default=0)
    def __str__(self):
        return self.user_name

class WeeklyTasks(models.Model):
    user_name=models.CharField(max_length=50)
    Weekly_tasks=models.CharField(max_length=120)
    completion = models.BooleanField(default=0)
    def __str__(self):
        return self.user_name

class MonthlyTasks(models.Model):
    user_name=models.CharField(max_length=50)
    Monthly_tasks=models.CharField(max_length=120)
    completion = models.BooleanField(default=0)
    def __str__(self):
        return self.user_name