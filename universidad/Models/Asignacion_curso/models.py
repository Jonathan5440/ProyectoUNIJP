from django.db import models
from universidad.Models.Catedratico.models import Catedratico
from universidad.Models.Curso.models import Curso

class Asignacion_curso(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    catedratico = models.ForeignKey(Catedratico, on_delete=models.CASCADE)
    horario = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.curso} - {self.catedratico}"

    class Meta:
        db_table = 'asignacion_curso'