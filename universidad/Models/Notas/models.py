from django.db import models
from universidad.Models.Inscripcion_alumno.models import Inscripcion_alumno

class Notas(models.Model):
    inscripcion = models.ForeignKey(Inscripcion_alumno, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    descripcion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.inscripcion} - {self.nota}"

    class Meta:
        db_table = 'notas'