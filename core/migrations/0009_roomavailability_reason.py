# Generated by Django 5.1.2 on 2024-10-23 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_roomavailability'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomavailability',
            name='reason',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
