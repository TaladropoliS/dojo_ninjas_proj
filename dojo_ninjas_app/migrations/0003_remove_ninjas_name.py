# Generated by Django 3.1.5 on 2021-02-14 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0002_ninjas_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ninjas',
            name='name',
        ),
    ]
