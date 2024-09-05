import json

from django.contrib.auth.models import Permission
from django.core.management.base import BaseCommand
from django.core.serializers import serialize




class Command(BaseCommand):
    help = 'Export data from the auth app'

    def handle(self, *args, **kwargs):
        # Получите данные из модели
        data = serialize('json', Permission.objects.all())

        # Запишите данные в файл с необходимыми параметрами
        with open('groups.py', 'w', encoding='utf-8') as file:
            json.dump(json.loads(data), file, sort_keys=False, indent=4, ensure_ascii=False)

        self.stdout.write(self.style.SUCCESS('Data exported successfully to groups.py'))