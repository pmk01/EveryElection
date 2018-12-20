# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-03 18:01
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("organisations", "0021_remove_old_police_forces")]

    operations = [
        migrations.CreateModel(
            name="DivisionGeography",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "geography",
                    django.contrib.gis.db.models.fields.MultiPolygonField(
                        geography=True, srid=4326
                    ),
                ),
                (
                    "division",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="geography",
                        to="organisations.OrganisationDivision",
                    ),
                ),
                (
                    "organisation",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="geography",
                        to="organisations.Organisation",
                    ),
                ),
            ],
        )
    ]
