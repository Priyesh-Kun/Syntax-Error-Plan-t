from django.db import models

# Create your models here.
class Users(models.Model):
    user_name=models.CharField(max_length=50)
    name=models.CharField(max_lenght=122)
    email=models.CharField(max_length=122)
    pass_word = models.CharField(max_length=20)
    def __str__(self):
        return self.name
