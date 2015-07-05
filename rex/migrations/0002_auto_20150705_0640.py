# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contact_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='enrolment_number',
            field=models.IntegerField(),
        ),
    ]
