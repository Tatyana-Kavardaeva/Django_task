# Generated by Django 5.1 on 2024-08-24 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dogs", "0005_remove_parent_year_born"),
    ]

    operations = [
        migrations.RenameField(
            model_name="parent",
            old_name="year_born_temp",
            new_name="year_born",
        ),
    ]
