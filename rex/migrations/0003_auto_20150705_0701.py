# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rex', '0002_auto_20150705_0640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contact_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='enrolment_number',
            field=models.CharField(max_length=8),
        ),
    ]
