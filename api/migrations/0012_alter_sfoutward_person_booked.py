# Generated by Django 3.2 on 2023-04-15 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20230409_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sfoutward',
            name='person_booked',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
