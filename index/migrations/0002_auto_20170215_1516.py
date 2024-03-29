# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-02-15 23:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('units', models.IntegerField(blank=True, default=180)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spaceLeft', models.IntegerField(blank=True)),
                ('classSize', models.IntegerField(blank=True)),
                ('code', models.IntegerField()),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
                ('dayOfWeek1', models.CharField(choices=[('MO', 'Monday'), ('TU', 'Tuesday'), ('WE', 'Wednesday'), ('TH', 'Thursday'), ('FR', 'Friday')], max_length=2)),
            ],
        ),
        migrations.RenameField(
            model_name='class',
            old_name='dayOfWeek',
            new_name='dayOfWeek1',
        ),
        migrations.AddField(
            model_name='class',
            name='code',
            field=models.CharField(default=datetime.datetime(2017, 2, 15, 23, 16, 23, 211000, tzinfo=utc), max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='class',
            name='dayOfWeek2',
            field=models.CharField(choices=[('MO', 'Monday'), ('TU', 'Tuesday'), ('WE', 'Wednesday'), ('TH', 'Thursday'), ('FR', 'Friday')], default=datetime.datetime(2017, 2, 15, 23, 16, 34, 526000, tzinfo=utc), max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='bot',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='section',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='index.Class'),
        ),
        migrations.AddField(
            model_name='major',
            name='requirements',
            field=models.ManyToManyField(related_name='required_for_major', to='index.Class'),
        ),
        migrations.AddField(
            model_name='major',
            name='users',
            field=models.ManyToManyField(related_name='major', to='index.Profile'),
        ),
    ]
