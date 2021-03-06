# Generated by Django 2.2.7 on 2020-01-20 22:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('price', models.FloatField()),
                ('category', models.CharField(max_length=30)),
                ('comments', models.PositiveIntegerField()),
                ('rate', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('plataform', models.CharField(max_length=10)),
            ],
        ),
    ]
