# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-27 14:20
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0047_auto_20180627_1243'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organisationgeography',
            options={'get_latest_by': 'start_date', 'ordering': ('-start_date',), 'verbose_name_plural': 'Organisation Geographies'},
        ),
        migrations.AlterField(
            model_name='organisationgeography',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='organisationgeography',
            name='geography',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='organisationgeography',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
