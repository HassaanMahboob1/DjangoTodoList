# Generated by Django 4.1 on 2022-08-19 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("List", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Person",
            new_name="Item",
        ),
    ]
