# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capability',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('status', models.CharField(max_length=255, choices=[(b'Approved', b'Approved'), (b'Draft', b'Draft'), (b'Retired', b'Retired')])),
                ('capability_num', models.DecimalField(null=True, max_digits=5, decimal_places=4, blank=True)),
                ('level', models.CharField(max_length=1, choices=[(b'0', b'Level 0'), (b'1', b'Level 1'), (b'2', b'Level 2'), (b'3', b'Level 3')])),
            ],
            options={
                'verbose_name_plural': 'Capabilities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('status', models.CharField(max_length=255, choices=[(b'Approved', b'Approved'), (b'Draft', b'Draft'), (b'Retired', b'Retired')])),
                ('domain_num', models.DecimalField(null=True, max_digits=5, decimal_places=4, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('status', models.CharField(max_length=255)),
                ('function_num', models.DecimalField(null=True, max_digits=5, decimal_places=4, blank=True)),
                ('capability', models.ForeignKey(to='backend.Capability')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255, null=True, blank=True)),
                ('status', models.CharField(max_length=255, choices=[(b'Approved', b'Approved'), (b'Draft', b'Draft'), (b'Retired', b'Retired')])),
                ('issue_num', models.DecimalField(null=True, max_digits=5, decimal_places=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Principle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('status', models.CharField(max_length=255, choices=[(b'Approved', b'Approved'), (b'Draft', b'Draft'), (b'Retired', b'Retired')])),
                ('principle_num', models.DecimalField(null=True, max_digits=5, decimal_places=4, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Proces',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('process_num', models.DecimalField(null=True, max_digits=5, decimal_places=4, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Processes',
            },
            bases=(models.Model,),
        ),
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
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resource_name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255, choices=[(b'Approved', b'Approved'), (b'Draft', b'Draft'), (b'Retired', b'Retired')])),
                ('resource_num', models.DecimalField(null=True, max_digits=5, decimal_places=4, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('status', models.CharField(max_length=255, choices=[(b'Approved', b'Approved'), (b'Draft', b'Draft'), (b'Retired', b'Retired')])),
                ('role_num', models.DecimalField(null=True, max_digits=5, decimal_places=4, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RoletoFunction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('status', models.CharField(max_length=255, choices=[(b'Approved', b'Approved'), (b'Draft', b'Draft'), (b'Retired', b'Retired')])),
                ('allocation', models.DecimalField(max_digits=5, decimal_places=2)),
                ('roletofunction_num', models.DecimalField(null=True, max_digits=5, decimal_places=4, blank=True)),
                ('function', models.ForeignKey(to='backend.Function')),
                ('role', models.ForeignKey(to='backend.Role')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('status', models.CharField(max_length=255, choices=[(b'Approved', b'Approved'), (b'Draft', b'Draft'), (b'Retired', b'Retired')])),
                ('owner', models.CharField(max_length=255)),
                ('vision_num', models.DecimalField(null=True, max_digits=5, decimal_places=4, blank=True)),
                ('project', models.ManyToManyField(to='backend.Project', null=True)),
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
        migrations.AddField(
            model_name='proces',
            name='project',
            field=models.ManyToManyField(to='backend.Project', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='principle',
            name='project',
            field=models.ManyToManyField(to='backend.Project', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='issue',
            name='project',
            field=models.ManyToManyField(to='backend.Project', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='function',
            name='project',
            field=models.ManyToManyField(to='backend.Project', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='domain',
            name='project',
            field=models.ManyToManyField(to='backend.Project', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='capability',
            name='domain',
            field=models.ManyToManyField(to='backend.Domain'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='capability',
            name='project',
            field=models.ManyToManyField(to='backend.Project', null=True),
            preserve_default=True,
        ),
    ]
