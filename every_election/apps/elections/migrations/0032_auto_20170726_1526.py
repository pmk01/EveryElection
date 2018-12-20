# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-26 15:26
from __future__ import unicode_literals

from django.db import migrations, models
import elections.models


class Migration(migrations.Migration):

    dependencies = [("elections", "0031_auto_20170726_1333")]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="uploaded_file",
            field=models.FileField(
                storage=elections.models.PdfS3Storage(), upload_to=""
            ),
        )
    ]
