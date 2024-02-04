# Generated by Django 5.0.1 on 2024-02-03 23:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_trainer_age_trainer_bmi_trainer_bmr'),
    ]

    operations = [
        migrations.CreateModel(
            name='FitnessProgram',
            fields=[
                ('program_id', models.AutoField(primary_key=True, serialize=False)),
                ('program_name', models.CharField(max_length=100)),
                ('program_day', models.CharField(max_length=50)),
                ('program_time', models.CharField(max_length=50)),
                ('program_pax', models.IntegerField()),
                ('program_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('program_images', models.ImageField(blank=True, null=True, upload_to='program_images/')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.trainer')),
            ],
        ),
    ]
