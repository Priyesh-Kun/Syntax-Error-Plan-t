from django.db import models

# Create your models here.
class Users(models.Model):
    user_name=models.CharField(max_length=50)
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    pass_word = models.CharField(max_length=20)
    pass_word_confirm = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class DailyTasks(models.Model):
    user_name=models.CharField(max_length=50)
    daily_tasks=models.CharField(max_length=120)
    def __str__(self):
        return self.user_name

class WeeklyTasks(models.Model):
    user_name=models.CharField(max_length=50)
    Weekly_tasks=models.CharField(max_length=120)
    def __str__(self):
        return self.user_name

class MonthlyTasks(models.Model):
    user_name=models.CharField(max_length=50)
    Monthly_tasks=models.CharField(max_length=120)
    def __str__(self):
        return self.user_name