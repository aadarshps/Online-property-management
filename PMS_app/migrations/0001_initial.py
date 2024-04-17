# Generated by Django 5.0.3 on 2024-04-17 11:05

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_no', models.CharField(max_length=30)),
                ('card_cvv', models.CharField(max_length=30)),
                ('expiry_date', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_owner', models.BooleanField(default=False)),
                ('is_cus', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Property_type', models.CharField(choices=[('Land', 'Land'), ('Home', 'Home'), ('Flat', 'Flat'), ('Villa', 'Villa'), ('Shops', 'Shops'), ('Garrage', 'Garrage'), ('Godown', 'Godown')], max_length=100)),
                ('Location', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Rent_amount', models.CharField(max_length=100)),
                ('Documents', models.FileField(upload_to='docs')),
                ('Image1', models.ImageField(upload_to='img1')),
                ('Image2', models.ImageField(upload_to='img2')),
                ('Image3', models.ImageField(upload_to='img3')),
                ('approval_status', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='customer', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=255)),
                ('Phone_Number', models.CharField(max_length=10)),
                ('Email_Id', models.EmailField(max_length=254)),
                ('Photo', models.ImageField(upload_to='pic')),
                ('Id_Card', models.FileField(upload_to='Id')),
                ('approval_status', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='owner', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Name', models.CharField(max_length=200)),
                ('Phone_No', models.CharField(max_length=10)),
                ('Address', models.CharField(max_length=255)),
                ('Email_Id', models.EmailField(max_length=254)),
                ('Photo', models.ImageField(upload_to='photo')),
                ('Id_Card', models.FileField(upload_to='id')),
                ('approval_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('feedback', models.TextField()),
                ('date', models.DateField()),
                ('reply', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMS_app.property')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMS_app.owner')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('paid_on', models.DateField(auto_now=True)),
                ('status', models.IntegerField(default=0)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMS_app.customer')),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='owner_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMS_app.owner'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMS_app.schedule')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment', to='PMS_app.customer')),
                ('user2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='PMS_app.owner')),
            ],
        ),
    ]
