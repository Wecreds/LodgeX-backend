# Generated by Django 5.1.2 on 2024-10-24 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_alter_payment_payment_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='payment_price',
            new_name='booking_price',
        ),
        migrations.AddField(
            model_name='payment',
            name='service_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
