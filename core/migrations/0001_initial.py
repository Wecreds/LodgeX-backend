# Generated by Django 5.1.2 on 2024-10-24 17:20

import core.models.user
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_status', models.IntegerField(choices=[(1, 'ACTIVE'), (2, 'CANCELED'), (3, 'COMPLETED')], default=1)),
                ('booking_date', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Booking',
                'verbose_name_plural': 'Bookings',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='DiscountCoupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('discount_percentage', models.IntegerField(default=0)),
                ('expiration_date', models.DateField()),
                ('description', models.CharField(blank=True, default=None, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Discount Coupon',
                'verbose_name_plural': 'Discount Coupons',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Cancellation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(default='No reason given.', max_length=255)),
                ('cancellation_date', models.DateField(default=django.utils.timezone.now)),
                ('booking', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.booking')),
            ],
            options={
                'verbose_name': 'Cancellation',
                'verbose_name_plural': 'Cancellations',
            },
        ),
        migrations.AddField(
            model_name='booking',
            name='discount_coupon',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.discountcoupon'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.IntegerField(choices=[(1, 'PENDING'), (2, 'PAID')], default=1)),
                ('booking_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('service_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('payment_method', models.IntegerField(choices=[(1, 'CREDIT CARD'), (2, 'DEBIT CARD'), (3, 'CASH'), (4, 'PIX')], default=4)),
                ('booking', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.booking')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('single_beds', models.IntegerField()),
                ('couple_beds', models.IntegerField()),
                ('price_by_day', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.CharField(max_length=400)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='core.category')),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
            },
        ),
        migrations.CreateModel(
            name='BookingRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.booking')),
                ('room', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='core.room')),
            ],
            options={
                'verbose_name': 'Booking Room',
                'verbose_name_plural': 'Bookings Rooms',
            },
        ),
        migrations.CreateModel(
            name='RoomAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('room_status', models.IntegerField(choices=[(1, 'RESERVED'), (2, 'MAINTENANCE')], default=1)),
                ('reason', models.CharField(blank=True, max_length=200, null=True)),
                ('booking', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.booking')),
                ('room', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.room')),
            ],
            options={
                'verbose_name': 'Room Availability',
                'verbose_name_plural': 'Room Availability',
            },
        ),
        migrations.CreateModel(
            name='RoomPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='uploader.image')),
                ('room', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.room')),
            ],
            options={
                'verbose_name': 'Room Photo',
                'verbose_name_plural': 'Room Photos',
            },
        ),
        migrations.CreateModel(
            name='BookingService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.booking')),
                ('service', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='core.service')),
            ],
            options={
                'verbose_name': 'Booking Service',
                'verbose_name_plural': 'Bookings Services',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(help_text='Email', max_length=255, unique=True, verbose_name='email')),
                ('name', models.CharField(blank=True, help_text='Username', max_length=255, null=True, verbose_name='name')),
                ('telephone', models.IntegerField(help_text="User's cell phone.", unique=True, verbose_name='telephone')),
                ('is_active', models.BooleanField(default=True, help_text='Indicates that this user is active.', verbose_name='User is active')),
                ('is_staff', models.BooleanField(default=False, help_text='Indicates that this user is a company employee.', verbose_name='User is an employee')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('personal_info', models.JSONField(default=core.models.user.User.jsonfield_default_value, help_text='Personal info about the User.', null=True)),
                ('document', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='uploader.image')),
                ('groups', models.ManyToManyField(blank=True, related_name='custom_user_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='custom_permission_user_set', to='auth.permission')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', core.models.user.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_status', models.IntegerField(blank=True, choices=[(1, 'PENDING'), (2, 'DECLINED'), (3, 'APPROVED')], default=1, null=True)),
                ('rating', models.DecimalField(decimal_places=1, default=1, max_digits=2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('comment', models.CharField(default='No comments.', max_length=255)),
                ('feedback_date', models.DateField(default=django.utils.timezone.now)),
                ('booking', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.booking')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.user')),
            ],
            options={
                'verbose_name': 'Feedback',
                'verbose_name_plural': 'Feedbacks',
            },
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='core.user'),
        ),
    ]
