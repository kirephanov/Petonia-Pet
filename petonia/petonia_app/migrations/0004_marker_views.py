# Generated by Django 3.2.7 on 2021-09-26 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petonia_app', '0003_alter_marker_telephone'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Просмотры'),
        ),
    ]