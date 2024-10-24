# Generated by Django 5.1.2 on 2024-10-24 17:36

import core.models.user
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='No category name given.', max_length=100),
        ),
        migrations.AlterField(
            model_name='discountcoupon',
            name='description',
            field=models.CharField(default='No description given.', max_length=200),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='comment',
            field=models.CharField(default='No comment given.', max_length=255),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='review_status',
            field=models.IntegerField(choices=[(1, 'PENDING'), (2, 'DECLINED'), (3, 'APPROVED')], default=1),
        ),
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.category'),
        ),
        migrations.AlterField(
            model_name='room',
            name='couple_beds',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.CharField(default='No description given.', max_length=400),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(default='No room name given.', max_length=100),
        ),
        migrations.AlterField(
            model_name='room',
            name='price_by_day',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='room',
            name='single_beds',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.CharField(default='No description given.', max_length=200),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(default='No service name given.', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='No user name given.', help_text='Username', max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='personal_info',
            field=models.JSONField(default=core.models.user.User.jsonfield_default_value, help_text='Personal info about the User.'),
        ),
        migrations.AlterField(
            model_name='user',
            name='telephone',
            field=models.IntegerField(blank=True, help_text="User's cell phone.", null=True, unique=True, verbose_name='telephone'),
        ),
    ]
