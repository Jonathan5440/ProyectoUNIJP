from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    creditos = models.IntegerField(default=3)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'curso'