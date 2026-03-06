from django.db import models
from universidad.Models.Alumno.models import Alumno
from universidad.Models.Asignacion_curso.models import Asignacion_curso

class Inscripcion_alumno(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    asignacion = models.ForeignKey(Asignacion_curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.alumno} - {self.asignacion}"

    class Meta:
        db_table = 'inscripcion_alumno'