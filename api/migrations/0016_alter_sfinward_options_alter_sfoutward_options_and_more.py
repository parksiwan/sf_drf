# Generated by Django 4.2.2 on 2023-06-30 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_sfinward_options_sfinward_location'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sfinward',
            options={'verbose_name': 'Inward Delivery', 'verbose_name_plural': 'Inward Delivery'},
        ),
        migrations.AlterModelOptions(
            name='sfoutward',
            options={'verbose_name': 'Outward Dispatch', 'verbose_name_plural': 'Outward Dispatch'},
        ),
        migrations.AlterModelOptions(
            name='sftask',
            options={'verbose_name': 'Remark', 'verbose_name_plural': 'Remarks'},
        ),
        migrations.AddField(
            model_name='sfinward',
            name='qty',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='sfinward',
            name='unit',
            field=models.CharField(max_length=20, null=True),
        ),
    ]