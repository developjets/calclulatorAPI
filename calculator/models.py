from django.db import models

# Create your models here.

class RequestLogs(models.Model):
    firstValue = models.IntegerField()
    secondValue = models.IntegerField()
    operationName = models.CharField(max_length=50)
    appName = models.CharField(max_length=50)

    def __str__(self):
        return self.appName