from django.db import models

class categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre


class producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=True)
    imagen = models.FileField(upload_to='productos', null=True, blank=True)

    def __str__(self):
        return self.nombre