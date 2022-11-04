from django.db import models

# Create your models here.
class familia(models.Model):
    nombre = models.CharField(max_length =50)
    edad = models.IntegerField()
    ultimo_log = models.TimeField(null = True)
    
    def __str__(self) -> str:
        return self.nombre
    