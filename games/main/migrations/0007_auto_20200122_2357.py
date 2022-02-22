# Generated by Django 2.2.6 on 2020-01-22 22:57

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200121_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='rate',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]),
        ),
    ]