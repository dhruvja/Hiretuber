# Generated by Django 3.2.1 on 2021-05-06 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiretubers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiretubers',
            name='phone',
            field=models.CharField(max_length=255),
        ),
    ]
