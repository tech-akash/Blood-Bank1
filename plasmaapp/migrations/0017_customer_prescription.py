# Generated by Django 3.2.6 on 2021-08-16 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plasmaapp', '0016_customer_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='prescription',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]