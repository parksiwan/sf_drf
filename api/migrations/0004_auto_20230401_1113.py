# Generated by Django 3.2 on 2023-04-01 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20230331_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sfoutward',
            name='booked_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sfoutward',
            name='dispatched_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]