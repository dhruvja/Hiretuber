# Generated by Django 3.2 on 2021-05-03 13:55

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0002_rename_youtubers_youtuber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='camera_type',
            field=models.CharField(choices=[('sony', 'sony'), ('nikon', 'nikon'), ('canon', 'canon')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='category',
            field=models.CharField(choices=[('coding', 'coding'), ('gaming', 'gaming'), ('cooking', 'cooking'), ('comedy', 'comedy'), ('Tech reviews', 'Tech reviews'), ('Vlogs', 'Vlogs')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='crew',
            field=models.CharField(choices=[('solo', 'solo'), ('small', 'small'), ('large', 'large')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(),
        ),
    ]
