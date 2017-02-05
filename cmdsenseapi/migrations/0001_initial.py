# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 23:40
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]