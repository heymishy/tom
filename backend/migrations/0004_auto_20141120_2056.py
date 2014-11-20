# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20141105_1926'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='capability',
            options={'verbose_name_plural': 'Capabilities'},
        ),
        migrations.AlterModelOptions(
            name='proces',
            options={'verbose_name_plural': 'Processes'},
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='name',
            new_name='resource_name',
        ),
        migrations.AddField(
            model_name='capability',
            name='capability_num',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='domain',
            name='domain_num',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='function',
            name='function_num',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='issue',
            name='issue_num',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='issue',
            name='status',
            field=models.CharField(default='Approved', max_length=255, choices=[(b'Approved', b'Approved'), (b'Draft', b'Draft'), (b'Retired', b'Retired')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='principle',
            name='principle_num',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='proces',
            name='process_num',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resource',
            name='resource_num',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='role',
            name='role_num',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='roletofunction',
            name='roletofunction_num',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='vision',
            name='vision_num',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='capability',
            name='description',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='capability',
            name='status',
            field=models.CharField(max_length=255, choices=[(b'Approved', b'Approved'), (b'Draft', b'Draft'), (b'Retired', b'Retired')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='domain',
            name='description',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='domain',
            name='status',
            field=models.CharField(max_length=255, choices=[(b'Approved', b'Approved'), (b'Draft', b'Draft'), (b'Retired', b'Retired')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='function',
            name='description',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='issue',
            name='description',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='principle',
            name='description',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='principle',
            name='status',
            field=models.CharField(max_length=255, choices=[(b'Approved', b'Approved'), (b'Draft', b'Draft'), (b'Retired', b'Retired')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proces',
            name='description',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resource',
            name='status',
            field=models.CharField(max_length=255, choices=[(b'Approved', b'Approved'), (b'Draft', b'Draft'), (b'Retired', b'Retired')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='role',
            name='description',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='role',
            name='status',
            field=models.CharField(max_length=255, choices=[(b'Approved', b'Approved'), (b'Draft', b'Draft'), (b'Retired', b'Retired')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='roletofunction',
            name='allocation',
            field=models.DecimalField(max_digits=5, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='roletofunction',
            name='description',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='roletofunction',
            name='status',
            field=models.CharField(max_length=255, choices=[(b'Approved', b'Approved'), (b'Draft', b'Draft'), (b'Retired', b'Retired')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vision',
            name='description',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vision',
            name='status',
            field=models.CharField(max_length=255, choices=[(b'Approved', b'Approved'), (b'Draft', b'Draft'), (b'Retired', b'Retired')]),
            preserve_default=True,
        ),
    ]
