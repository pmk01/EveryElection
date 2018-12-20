# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-07 14:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("organisations", "0025_organisationdivisionset_territory_code")]

    operations = [
        migrations.AlterUniqueTogether(
            name="organisationdivision",
            unique_together=set(
                [("organisation", "divisionset", "official_identifier")]
            ),
        )
    ]
