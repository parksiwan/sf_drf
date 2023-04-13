# Generated by Django 3.2 on 2023-03-31 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SFOutward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.CharField(max_length=30)),
                ('product_type', models.CharField(max_length=10)),
                ('etd', models.DateTimeField(auto_now_add=True)),
                ('freight_company', models.CharField(max_length=30)),
                ('booked_date', models.DateTimeField(auto_now_add=True)),
                ('dispatched_date', models.DateTimeField(auto_now_add=True)),
                ('person_booked', models.CharField(max_length=20)),
                ('person_dispatched', models.CharField(max_length=20)),
                ('memo', models.CharField(max_length=300)),
            ],
        ),
    ]
