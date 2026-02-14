from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Driver(models.Model):
    usario=models.OneToOneField(User,on_delete=models.CASCADE)
    Telefono=models.CharField(max_length=20)
    No_Licencia=models.CharField(max_length=20)
    Matricula=models.CharField(max_length=20)
    Activado=models.BooleanField(default=True)
    def __str__(self):
        return self.usario.username