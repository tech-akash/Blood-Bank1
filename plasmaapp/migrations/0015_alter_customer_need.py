# Generated by Django 3.2.6 on 2021-08-14 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plasmaapp', '0014_auto_20210813_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='need',
            field=models.CharField(blank=True, choices=[('None', 'None'), ('Acceptor', 'Acceptor'), ('Donator', 'Donator')], default='None', max_length=20, null=True, verbose_name='Need'),
        ),
    ]
