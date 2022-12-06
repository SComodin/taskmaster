import datetime
from tasks.models import Task

from django.core.management.base import BaseCommand

import tqdm


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        hoy = datetime.datetime.today()
        hoy_pero_hace_siete_dias = hoy - datetime.timedelta(days=7)
        tareas = (
            Task.objects
            .exclude(priority='H')
            .exclude(finished=True)
            .filter(due_date__gte=hoy_pero_hace_siete_dias)
            .filter(due_date__lte=hoy)
        )
        for t in tqdm(tareas):
            t.priority = 'H'
            t.save()
            print(t.due_date, t.priority, t)