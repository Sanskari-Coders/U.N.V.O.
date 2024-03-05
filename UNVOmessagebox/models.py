from django.db import models

# Create your models here.

class Messages(models.Model):
    mid=models.AutoField(primary_key=True)
    message=models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.mid}"