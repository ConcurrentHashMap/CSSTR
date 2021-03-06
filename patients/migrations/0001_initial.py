# Generated by Django 3.0.4 on 2020-03-21 15:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=6)),
                ('email', models.CharField(default='', max_length=100)),
                ('num_people', models.IntegerField(default=1)),
                ('car', models.BooleanField(default=True)),
                ('license_plate', models.CharField(default='', max_length=10)),
                ('firstname', models.CharField(default='', max_length=100)),
                ('lastname', models.CharField(default='', max_length=100)),
                ('birthdate', models.DateField(default=django.utils.timezone.now)),
                ('zip', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=100)),
                ('doctor', models.CharField(default='', max_length=100)),
                ('insurance', models.CharField(default='', max_length=100)),
                ('positive_contact', models.BooleanField(default=True)),
                ('tested', models.BooleanField(default=False)),
                ('confirmed', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
