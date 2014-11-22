# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20141122_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='project',
            field=models.ManyToManyField(to='backend.Project', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='roletofunction',
            name='function',
            field=models.ForeignKey(blank=True, to='backend.Function', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='roletofunction',
            name='role',
            field=models.ForeignKey(blank=True, to='backend.Role', null=True),
            preserve_default=True,
        ),
    ]
