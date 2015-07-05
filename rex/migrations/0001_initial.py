# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room_number', models.CharField(max_length=4)),
                ('description', models.TextField()),
                ('preference', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('enrolment_number', models.IntegerField(max_length=8)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.IntegerField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='user',
            field=models.ForeignKey(to='rex.User'),
        ),
    ]
