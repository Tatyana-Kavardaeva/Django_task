# Generated by Django 4.2.2 on 2024-08-31 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("dogs", "0006_rename_year_born_temp_parent_year_born"),
    ]

    operations = [
        migrations.AddField(
            model_name="dog",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                help_text="Укажите владельца собаки",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец",
            ),
        ),
    ]
