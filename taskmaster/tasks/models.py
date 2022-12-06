from django.db import models
from django.utils import timezone
import datetime


def hoy():
    return timezone.now().date()


class Project(models.Model):

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['code']

    name = models.CharField(max_length=250)
    code = models.SlugField(max_length=4, unique=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.code}: {self.description}'

    def progress(self):
        total_time = self.end_date - self.start_date
        today = datetime.date.today()
        time_passed = today - self.start_date
        progress = (float(time_passed.days) * 100.0) / float(total_time.days)
        return round(progress, 2)


class Task(models.Model):

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering = ['-orden', 'name']

    name = models.CharField(max_length=250)
    finished = models.BooleanField(default=False)
    orden = models.IntegerField(default=100)
    priority = models.CharField(
        max_length=1,
        choices=[
            ('H', 'Alta'),
            ('N', 'Normal'),
            ('L', 'Baja'),
        ],
        default='N',
    )
    color = models.CharField(
        max_length=6,
        choices=[
            ('blue', 'Azul Marino'),
            ('red', 'Rojo'),
            ('orange', 'Naranja'),
            ('green', 'Verde'),
        ],
        default='blue',
        )
    due_date = models.DateField(
        blank=True,
        null=True,
        default=None,
    )
    project = models.ForeignKey(
        Project,
        blank=True,
        null=True,
        default=None,
        on_delete=models.SET_NULL,
        )

    def __str__(self):
        return self.name

    def is_due(self) -> bool:
        if self.due_date is None:
            return False
        return self.due_date <= hoy()
