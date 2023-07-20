from django.db import models

class Inscrito(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    telefono = models.IntegerField()
    fecha_hora_ins = models.DateTimeField()
    institucion = models.CharField(max_length=50)
    estado = models.CharField(max_length=10)
    observacion = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return str(self.id)+ ""+ self.nombre + "(Instituto: "+ str(self.institucion) + ")"
