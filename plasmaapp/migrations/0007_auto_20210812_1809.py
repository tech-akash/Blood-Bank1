# Generated by Django 3.2.6 on 2021-08-12 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plasmaapp', '0006_alter_accept_dayofaccept'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin1',
        ),
        migrations.AddField(
            model_name='accept',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('GotIt', 'GotIt'), ('Rejected', 'Rejected')], default='Pending', max_length=20, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='donate',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Donated', 'Donated'), ('Rejected', 'Rejected')], default='Pending', max_length=20, verbose_name='Status'),
        ),
    ]
