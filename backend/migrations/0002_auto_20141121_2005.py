# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capability',
            name='level',
            field=models.CharField(default=b'Approved', max_length=1, choices=[(b'0', b'Level 0'), (b'1', b'Level 1'), (b'2', b'Level 2'), (b'3', b'Level 3')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='capability',
            name='status',
            field=models.CharField(default=b'Approved', max_length=255, choices=[(b'Approved', b'Approved'), (b'Draft', b'Draft'), (b'Retired', b'Retired')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='domain',
            name='status',
            field=models.CharField(default=b'Approved', max_length=255, choices=[(b'Approved', b'Approved'), (b'Draft', b'Draft'), (b'Retired', b'Retired')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='function',
            name='status',
            field=models.CharField(default=b'Approved', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(default=b'Approved', max_length=255, choices=[(b'Approved', b'Approved'), (b'Draft', b'Draft'), (b'Retired', b'Retired')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='principle',
            name='status',
            field=models.CharField(default=b'Approved', max_length=255, choices=[(b'Approved', b'Approved'), (b'Draft', b'Draft'), (b'Retired', b'Retired')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(default=b'Approved', max_length=255, choices=[(b'Approved', b'Approved'), (b'Draft', b'Draft'), (b'Retired', b'Retired')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resource',
            name='status',
            field=models.CharField(default=b'Approved', max_length=255, choices=[(b'Approved', b'Approved'), (b'Draft', b'Draft'), (b'Retired', b'Retired')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='role',
            name='status',
            field=models.CharField(default=b'Approved', max_length=255, choices=[(b'Approved', b'Approved'), (b'Draft', b'Draft'), (b'Retired', b'Retired')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='roletofunction',
            name='status',
            field=models.CharField(default=b'Approved', max_length=255, choices=[(b'Approved', b'Approved'), (b'Draft', b'Draft'), (b'Retired', b'Retired')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vision',
            name='status',
            field=models.CharField(default=b'Approved', max_length=255, choices=[(b'Approved', b'Approved'), (b'Draft', b'Draft'), (b'Retired', b'Retired')]),
            preserve_default=True,
        ),
    ]
