# Generated by Django 3.2.6 on 2021-08-12 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plasmaapp', '0008_auto_20210812_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accept',
            name='dayofaccept',
            field=models.DateField(blank=True, null=True, verbose_name='Day of Accepting'),
        ),
        migrations.AlterField(
            model_name='donate',
            name='dayofdonate',
            field=models.DateField(blank=True, null=True, verbose_name='Day of Donating'),
        ),
    ]
