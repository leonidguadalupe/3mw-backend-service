# Generated by Django 2.2.4 on 2019-09-01 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20190827_1548'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='datapoint',
            unique_together={('plant', 'datetime_generated')},
        ),
    ]
