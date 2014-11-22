# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0003_auto_20141122_0949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='function',
            name='project',
        ),
        migrations.RemoveField(
            model_name='vision',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='assigned_to',
            field=models.ManyToManyField(default=0, related_name='assigned_to', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resource',
            name='project',
            field=models.ManyToManyField(to='backend.Project', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='role',
            name='project',
            field=models.ManyToManyField(to='backend.Project', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='created_by',
            field=models.ForeignKey(related_name='created_by', default=0, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
