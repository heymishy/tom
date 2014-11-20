# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20141120_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capability',
            name='project',
            field=models.ManyToManyField(to='backend.Project', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='domain',
            name='project',
            field=models.ManyToManyField(to='backend.Project', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='function',
            name='project',
            field=models.ManyToManyField(to='backend.Project', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='issue',
            name='project',
            field=models.ManyToManyField(to='backend.Project', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='principle',
            name='project',
            field=models.ManyToManyField(to='backend.Project', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proces',
            name='project',
            field=models.ManyToManyField(to='backend.Project', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vision',
            name='project',
            field=models.ManyToManyField(to='backend.Project', null=True),
            preserve_default=True,
        ),
    ]
