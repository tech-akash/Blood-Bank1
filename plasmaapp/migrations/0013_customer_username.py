# Generated by Django 3.2.6 on 2021-08-13 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plasmaapp', '0012_auto_20210813_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='username',
            field=models.CharField(default='hii', max_length=200, verbose_name='Username'),
        ),
    ]
