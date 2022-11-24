# Generated by Django 3.2.16 on 2022-11-24 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konohagym', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excercise',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='excercise',
            name='image',
            field=models.ImageField(blank=True, upload_to='excercises', verbose_name='Ejemplo'),
        ),
        migrations.AlterField(
            model_name='muscle',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='muscle',
            name='image',
            field=models.ImageField(blank=True, upload_to='muscles'),
        ),
    ]