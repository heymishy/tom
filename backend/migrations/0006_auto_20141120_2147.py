# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20141120_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('proj_name', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.CharField(max_length=255, null=True, blank=True)),
                ('status', models.CharField(max_length=255, choices=[(b'Approved', b'Approved'), (b'Draft', b'Draft'), (b'Retired', b'Retired')])),
                ('project_num', models.DecimalField(null=True, max_digits=5, decimal_places=4, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='capability',
            name='project',
            field=models.ForeignKey(to='backend.Project', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='domain',
            name='project',
            field=models.ForeignKey(to='backend.Project', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='function',
            name='project',
            field=models.ForeignKey(to='backend.Project', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(to='backend.Project', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='principle',
            name='project',
            field=models.ForeignKey(to='backend.Project', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='proces',
            name='project',
            field=models.ForeignKey(to='backend.Project', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='vision',
            name='project',
            field=models.ForeignKey(to='backend.Project', null=True),
            preserve_default=True,
        ),
    ]
