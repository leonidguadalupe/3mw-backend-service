# Generated by Django 2.2.4 on 2019-09-01 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20190901_1337'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='datapoint',
            index=models.Index(fields=['plant', 'datetime_generated'], name='backend_dat_plant_i_8d0c8f_idx'),
        ),
    ]
