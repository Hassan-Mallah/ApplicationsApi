from django.db import models

# Create your models here.
class Application(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    key = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return self.name