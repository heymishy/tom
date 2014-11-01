# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoletoFunction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('allocation', models.IntegerField()),
                ('function', models.ForeignKey(to='backend.Function')),
                ('role', models.ForeignKey(to='backend.Role')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='role',
            name='performs_func',
            field=models.ManyToManyField(to='backend.Function', through='backend.RoletoFunction'),
            preserve_default=True,
        ),
    ]
