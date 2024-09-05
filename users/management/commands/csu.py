import json
from django.core.management import call_command
from io import StringIO

# Создайте буфер для хранения данных
output = StringIO()
call_command('dumpdata', 'auth', stdout=output)

# Получите данные и сохраните их в файл с нужной кодировкой
data = output.getvalue()
with open('groups.json', 'w', encoding='utf-8') as f:
    f.write(data)

print("Данные успешно экспортированы в groups.json с кодировкой UTF-8.")