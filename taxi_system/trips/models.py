from django.db import models
from accounts.models import Driver

# Create your models here.
class Trip(models.Model):
    STATUS_CHOICES=[('encourso','Encourso'),('completado','Completado')]
    conductor=models.ForeignKey(Driver,on_delete=models.CASCADE)
    lugar_de_recogida=models.CharField(max_length=50)
    destino=models.CharField(max_length=50)
    hora_inicio=models.DateTimeField()
    hora_final=models.DateTimeField(null=True,blank=True)
    distancia=models.FloatField(null=True,blank=True)
    dinero=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
    estatuto=models.CharField(max_length=20,choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.conductor} - {self.estatuto}"
