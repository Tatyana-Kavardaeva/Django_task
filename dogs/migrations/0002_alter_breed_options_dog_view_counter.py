# Generated by Django 5.0.7 on 2024-08-10 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dogs", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="breed",
            options={"verbose_name": "Порода", "verbose_name_plural": "Породы"},
        ),
        migrations.AddField(
            model_name="dog",
            name="view_counter",
            field=models.PositiveIntegerField(
                default=0,
                help_text="Укажите количество просмотров",
                verbose_name="Просмотры",
            ),
        ),
    ]
