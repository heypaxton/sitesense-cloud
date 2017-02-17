# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 03:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmdsenseapi', '0005_auto_20170205_0118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=100)),
                ('description', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('worksite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdsenseapi.Worksite')),
            ],
            options={
                'db_table': 'area',
                'ordering': ('created_at',),
            },
        ),
        migrations.RemoveField(
            model_name='device',
            name='worksite',
        ),
        migrations.RemoveField(
            model_name='reading',
            name='device',
        ),
        migrations.DeleteModel(
            name='Device',
        ),
    ]
