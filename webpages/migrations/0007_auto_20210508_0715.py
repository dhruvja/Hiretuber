# Generated by Django 3.2.1 on 2021-05-08 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0006_aboutus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='first_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='second_description',
            field=models.TextField(),
        ),
    ]
