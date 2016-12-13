# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-13 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('clicks', models.IntegerField(default=0)),
            ],
        ),
    ]
