from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker
import random

from universidad.Models.Alumno.models import Alumno
from universidad.Models.Catedratico.models import Catedratico
from universidad.Models.Curso.models import Curso
from universidad.Models.Asignacion_curso.models import Asignacion_curso
from universidad.Models.Inscripcion_alumno.models import Inscripcion_alumno
from universidad.Models.Notas.models import Notas

fake = Faker('es_MX')

class Command(BaseCommand):
    help = 'Poblar la base de datos con 10,000 registros'

    def handle(self, *args, **kwargs):
        self.stdout.write('🚀 Iniciando población de base de datos...')
        with transaction.atomic():
            self.crear_catedraticos(50)
            self.crear_cursos()
            self.crear_asignaciones()
            self.crear_alumnos(10000)
            self.crear_inscripciones_y_notas()
        self.stdout.write(self.style.SUCCESS('✅ Base de datos poblada exitosamente!'))

    def crear_catedraticos(self, n):
        self.stdout.write(f'  Creando {n} catedráticos...')
        for _ in range(n):
            Catedratico.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
                phone=fake.phone_number()[:20],
            )

    def crear_cursos(self):
        self.stdout.write('  Creando cursos...')
        cursos = [
            'Matemáticas', 'Física', 'Química', 'Historia', 'Literatura',
            'Programación', 'Base de Datos', 'Redes', 'Inglés', 'Filosofía',
            'Biología', 'Estadística', 'Economía', 'Contabilidad', 'Derecho',
            'Psicología', 'Arquitectura', 'Diseño', 'Marketing', 'Administración'
        ]
        for nombre in cursos:
            Curso.objects.create(
                nombre=nombre,
                descripcion=fake.text(max_nb_chars=200),
                creditos=random.randint(2, 5),
            )

    def crear_asignaciones(self):
        self.stdout.write('  Creando asignaciones...')
        catedraticos = list(Catedratico.objects.all())
        cursos = list(Curso.objects.all())
        horarios = ['Lunes 7:00-9:00', 'Martes 9:00-11:00', 'Miércoles 13:00-15:00',
                    'Jueves 15:00-17:00', 'Viernes 7:00-9:00']
        for curso in cursos:
            Asignacion_curso.objects.create(
                curso=curso,
                catedratico=random.choice(catedraticos),
                horario=random.choice(horarios),
            )

    def crear_alumnos(self, n):
        self.stdout.write(f'  Creando {n} alumnos...')
        alumnos = []
        for _ in range(n):
            alumnos.append(Alumno(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
                phone=fake.phone_number()[:20],
                gender=random.choice(['M', 'F']),
                birth_date=fake.date_of_birth(minimum_age=17, maximum_age=30),
                is_active=random.choice([True, True, True, False]),
            ))
        Alumno.objects.bulk_create(alumnos, batch_size=500)

    def crear_inscripciones_y_notas(self):
        self.stdout.write('  Creando inscripciones y notas...')
        alumnos = list(Alumno.objects.all())
        asignaciones = list(Asignacion_curso.objects.all())
        inscripciones = []
        for alumno in alumnos:
            for asignacion in random.sample(asignaciones, random.randint(1, 4)):
                inscripciones.append(Inscripcion_alumno(
                    alumno=alumno,
                    asignacion=asignacion,
                ))
        Inscripcion_alumno.objects.bulk_create(inscripciones, batch_size=500, ignore_conflicts=True)

        notas = []
        for inscripcion in Inscripcion_alumno.objects.all():
            notas.append(Notas(
                inscripcion=inscripcion,
                nota=round(random.uniform(51, 100), 2),
                descripcion=random.choice(['Parcial 1', 'Parcial 2', 'Final', '']),
            ))
        Notas.objects.bulk_create(notas, batch_size=500)