# Generated by Django 4.2.2 on 2023-07-08 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_alter_sfinward_options_alter_sfoutward_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sftask',
            name='assignee',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
