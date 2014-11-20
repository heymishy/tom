# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20141120_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capability',
            name='capability_num',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='domain',
            name='domain_num',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='function',
            name='function_num',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='issue',
            name='description',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='principle',
            name='principle_num',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proces',
            name='process_num',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resource',
            name='resource_num',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='role',
            name='role_num',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='roletofunction',
            name='roletofunction_num',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vision',
            name='vision_num',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4, blank=True),
            preserve_default=True,
        ),
    ]
