# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20141122_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='description',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='role',
            name='performs_func',
            field=models.ManyToManyField(to='backend.Function', null=True, through='backend.RoletoFunction', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='roletofunction',
            name='allocation',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='roletofunction',
            name='created_by',
            field=models.ForeignKey(default=0, blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='roletofunction',
            name='name',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
