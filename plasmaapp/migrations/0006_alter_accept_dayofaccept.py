# Generated by Django 3.2.6 on 2021-08-12 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plasmaapp', '0005_alter_accept_dayofaccept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accept',
            name='dayofaccept',
            field=models.DateField(verbose_name='Day of Accepting'),
        ),
    ]
